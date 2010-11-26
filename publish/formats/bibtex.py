"This module implements input/output for BibTeX."

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-10-05 -- 2008-11-11"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

import re

from publish.common import pstr
from publish import config

# Pattern used for extracting the BibTeX-fields
_entry_list = "|".join([entry_type for entry_type in config.get("entrytype_attributes")])
_start_pattern = re.compile('^@(%s){(.*?)\s*,' % _entry_list, re.IGNORECASE) 

# Pattern used for extracting everything before and after the "="-sign
#_block_pattern = re.compile('\s*(.*?)\s*=\s*{(.*?)}\s*,')

# Pattern used for extracting attribute
_attribute_pattern = re.compile('\s*,*(.*?)\s*=\s*')

def read(text):
    "Extract papers from text and return papers as a list of dictionaries."

    print ""
    print "Importing papers from BibTeX"
    print "----------------------------"
    print ""

    papers = []
    position = 0
    lines = text.split("\n")
    for line in lines:

        # Look for start of paper
        match = _start_pattern.search(line)
        if not match is None:
            
            # Extract entry-type and key
            groups = match.groups()
            (entry_type, key) = groups

            # Make sure every entry-type is written in lower-case letters
            entry_type = entry_type.lower()
            
            # Look for starting point
            start = position + 1 + len(entry_type) + 1 + len(key) + 1 + 1

            # Look for the end point, by counting the braces
            num_left_braces = 1
            num_right_braces= 0
            value_start = []
            value_end = []
            for end in range(start, len(text)):

                # Count braces
                if text[end] == "{":
                    num_left_braces += 1
                elif text[end] == "}":
                    num_right_braces += 1

                # Mark positions for attribute values
                if text[end] == "{" and num_left_braces == num_right_braces + 2:
                    value_start.append(end - start)
                elif text[end] == "}" and num_left_braces == num_right_braces + 1:
                    value_end.append(end - start)
                
                # Found end of paper, done
                if num_left_braces == num_right_braces:
                    break

            # Extract the block, containing the required fields
            block = text[start:end]

            # Parse block
            paper = _parse_paper(block, value_start, value_end)

            # Check that the block contains all required fields
            paper["entrytype"] = entry_type
            paper["key"] = key

            # Check that paper has all required attributes
            _check_paper(paper)

            # Extract category
            paper["category"] = _extract_category(paper)

            # Extract authors as tuple from string
            if "author" in paper:
                _extract_authors(paper, "author")

            # Extract editors as tuple from string
            if "editor" in paper:
                _extract_authors(paper, "editor")

            # Add paper (a dictionary) to list of papers
            papers.append(paper)

        # Steps to next line
        position += len(line) + 1

    # Return list of papers
    return papers
        
def write(papers):
    "Format the given list of papers in the BibTeX format."
    
    text = ""

    for (i, paper) in enumerate(papers):
        entry_type = config.get("category2entrytype")[paper["category"]]
        if "key" in paper:
            key = paper["key"]
        else:
            key = "paper%d" % i
        text += "@%s{%s,\n" % (entry_type, key)
        for attribute in paper:
            if attribute in ("entrytype", "key"):
                continue
            elif attribute == "author":
                value = " and ".join(paper["author"])
            elif attribute == "editor":
                value = " and ".join(paper["editor"])
            else:
                value = str(paper[attribute])
            text += "  %s = {%s},\n" % (attribute, value)  
        text += "}\n"
        if not paper == papers[-1]:
            text += "\n"

    return text

def _parse_paper(block, value_start, value_end):
    "Parse paper attributes"

    # Check lists of positions, should be of equal size
    if not len(value_start) == len(value_end):
        raise RuntimeError, "Syntax error in BibTeX file, unbalanced braces."

    # Extract attributes and values
    paper = {}
    for i in range(len(value_start)):

        # Extract attribute
        if i == 0:
            attribute = block[0:value_start[0]]
        else:
            attribute = block[value_end[i - 1] + 1:value_start[i]]
        match = _attribute_pattern.search(attribute)
        if match is None:
            raise RuntimeError, "Syntax error in BibTeX file, missing attribute name."
        groups = match.groups()
        attribute = groups[0].lower()

        # Extract value
        value = block[value_start[i] + 1:value_end[i]].replace("\r", " ").replace("\n", " ").strip()

        # Set attribute and value
        paper[attribute] = value

    # Return a dictionary containing information about one paper
    return paper

def _check_paper(paper):
    "Check paper"

    print "Found paper: %s" % pstr(paper)

    invalid = False

    # Check that all values are ok (no stray {})
    for attribute in paper:
        value = paper[attribute]
        num_left_braces = 0
        num_right_braces = 0
        for c in value:
            if c == "{":
                num_left_braces += 1
            elif c == "}":
                num_right_braces += 1
            if num_left_braces < num_right_braces:
                invalid = True
                print '  Misplaced "{}" or "," in BibTeX entry.'
                break

    # Check that paper has all required attributes
    entry_type = paper["entrytype"]
    key = paper["key"]
    attributes = config.get("entrytype_attributes")[entry_type]
    for attribute in attributes:
        # Check if the required field is a tuple and at least one field is used 
        if isinstance(attribute, tuple):
            if not len([f for f in attribute if f in paper]) >= 1:
                print '  Missing required attribute(s) "%s" for paper "%s"' % ('"/"'.join(attribute), key)
                invalid = True
        elif not attribute in paper:
            print '  Missing required attribute "%s" for paper "%s"' % (attribute, key)
            invalid = True

    if invalid:
        paper["invalid"] = True
        print "  Skipping paper. Correct the above error(s) and import the paper again."
        if not config.get("autofix"):
            raw_input("  Press return to continue.")

def _extract_authors(paper, attribute):
    "Extract authors as tuple from string"

    names = paper[attribute].split(" and ")

    authors = []
    for name in names:
        name = name.strip()

        # Handle case Last, First
        if "," in name:
            words = name.split(",")
            if not len(words) == 2:
                paper["invalid"] = True
                print "  Incorrectly formatted author string:", name
                if config.get("autofix"):
                    print "  Skipping paper."
                else:
                    raw_input("  Skipping paper, press return to continue.")
            words.reverse()
            name = " ".join([w.strip() for w in words])
            
        # Add missing . for initials and cleanup spaces
        words = name.split(" ")
        new_words = []
        for word in words:
            word = word.strip()
            if len(word) == 1:
                new_words.append(word + ".")
            elif len(word) > 1:
                new_words.append(word)
        name = " ".join(new_words)
            
        authors.append(name)        

    paper[attribute] = tuple(authors)

def _extract_category(paper):
    "Extract category for paper"

    # Check if category is supported
    entry_type = paper["entrytype"]
    entrytype2category = config.get("entrytype2category")
    if not entry_type in entrytype2category:
        raise RuntimeError, 'Entry type "%s" not supported.' % entry_type

    # Check default mapping
    category = entrytype2category[entry_type]
    if not category is None:
        return category

    # Special case: book or edited
    if entry_type == "book":
        if "editor" in paper:
            paper["author"] = paper["editor"]
            del paper["editor"]
            return "edited"
        else:
            return "books"

    # Special case: phdthesis
    if entry_type == "phdthesis":
        paper["thesistype"] = "phd"
        return "theses"

    # Special case: mscthesis
    if entry_type == "mastersthesis":
        paper["thesistype"] = "msc"
        return "theses"

    # Special case: misc
    if entry_type == "misc":
        if "code" in paper:
            return "courses"
        elif "meeting" in paper:
            return "talks"
        else:
            return "misc"

    raise RuntimeError, "Unhandled special case for BibTeX entry type."
