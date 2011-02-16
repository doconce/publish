"This module implements output for HTML."

__author__ = "Anders Logg <logg@simula.no>"
__date__ = "2009-07-31 -- 2009-08-18"
__copyright__ = "Copyright (C) 2009 Anders Logg"
__license__  = "GNU GPL version 3 or any later version"

from publish import config

def write(papers):
    "Format the given list of papers in HTML format."

    text = ""

    # Get formatting rule
    html_format = config.get("html_format")

    # Get PDF directory
    pdf_dir = config.get("pdf_dir")

    # Iterate over categories
    categories = config.get("categories")
    current_paper = 0
    for category in categories:

        # Extract papers in category
        category_papers = [paper for paper in papers if paper["category"] == category]
        if len(category_papers) == 0:
            continue

        # Write category
        category_headings = config.get("category_headings")
        text += "<h2>%s</h2>\n\n" % category_headings[category]
        text += "<ol class=\"publish_list\">\n\n"

        # Iterate over papers in category
        for paper in category_papers:

            # Format paper entry
            paper_entry = html_format[category](paper)

            # Filter entry from special characters
            paper_entry = _filter(paper_entry)

            # Set directory to papers (a bit of a hack)
            paper_entry = paper_entry.replace("papers/", pdf_dir + "/")

            # Write entry for paper
            text += "<li class=\"publish_item\">\n" + paper_entry + "</li>\n"

        # Write end of list
        text += "</ol>\n"

    return text

def _filter(s):
    "Filter string for special characters."

    # List of replacements
    replacements = [("--", "&ndash;"),
                    ("\\ae", "ae"),
                    ("$", ""),
                    ("\\mathrm", ""),
                    ('\\aa', '&aring;'),
                    ('\\AA', '&Aring;'),
                    ('\\"a', '&auml;'),
                    ('\\"A', '&Auml;'),
                    ('\\"o', '&ouml;'),
                    ('\\"O', '&Ouml;')]

    # Iterate over replacements
    for (a, b) in replacements:
        s = s.replace(a, b)

    return s
