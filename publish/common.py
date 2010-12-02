"Some common utility functions"

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-10 -- 2008-11-11"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

from log import warning

import shlex

def is_valid(paper):
    "Check if paper is valid"
    
    if "invalid" in paper and paper["invalid"]:
        return False
    else:
        return True

def is_duplicate(paper):
    "Check if paper is a duplicate"

    if "duplicate" in paper and paper["duplicate"]:
        return True
    else:
        return False

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

    words = shlex.split(author)
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
