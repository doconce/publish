"Some common utility functions"

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-10 -- 2008-11-11"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

# Last modified: 2012-08-30
# Modified by Anders Logg 2012
# Modified by Benjamin Kehlet 2012

from log import warning
import StringIO, csv

from publish import config

def is_valid(paper):
    "Check if paper is valid"
    return not ("invalid" in paper and paper["invalid"])


def is_duplicate(paper):
    "Check if paper is a duplicate"
    return "duplicate" in paper and paper["duplicate"]


def is_allowed_duplicate(paper1, paper2) :
    "Check if papers are allowed duplicates"
    return (("allowed_duplicates" in paper1 and paper2["key"] in paper1["allowed_duplicates"]) or
           ("allowed_duplicates" in paper2 and paper1["key"] in paper2["allowed_duplicates"]))

def pstr(paper):
    "Return a simple string representation of the paper"

    s = "(%s) - %s" % (paper.get("key", "No key"),
                       paper.get("title", "No title"))

    if len(s) > 75 :
        s = s[:75]+"..."

    return s
    if "title" in paper:
        s = paper["title"]
        n = 75
        if len(s) > n:
            s = s[:n] + "..."
    else:
        s = "Unknown"
    return s

def short_author(author):
    "Abbreviate author name with initials"

    # Use the csv module to split the.
    # Seems unnatural, but it respects quotes
    # and does what we want, as opposed to the native
    # string functions.
    input = StringIO.StringIO(author)
    words = csv.reader(input, delimiter=' ').next()

    # This is an alternative, but leaves empty string
    # in the result list
    # words = author.split('\"')

    new_words = []
    for word in words[:-1]:
        if word == "":
            continue
        new_words.append(find_initials(word, author))
    return " ".join(new_words) + " " + words[-1]

def find_initials(name, author):
    "Generate initial string for name"

    if name == "":
        return ""

    # Call recursively for hyphen in name
    if "-" in name:
        return "-".join([find_initials(part, author) for part in name.split("-")])

    # Simple case: just a plain character
    if name[0].isalpha():
        return name[0] + "."

    # Nasty case: begins with "{"
    for i in range(len(name)):
        if name[i] == "}":
            return name[:i + 1] + "."

    # Unhandled case, just return full name
    warning("Unable to abbreviate author name, too complex: " + str(author))
    return name

def ordered_attributes(paper, ignores=[]):
    "Return list of ordered attributes for paper"
    attributes = []
    for attribute in config.get("ordered_attributes"):
        if attribute in paper and not attribute in ignores:
            attributes.append(attribute)
    for attribute in paper:
        if not attribute in attributes and not attribute in ignores:
            attributes.append(attribute)
    return attributes
