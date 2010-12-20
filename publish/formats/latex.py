"This module implements input/output for LaTeX."

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-06 -- 2008-11-12"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

from publish import config

def write(papers, sort_func=None):
    "Format the given list of papers in the LaTeX format."

    text = ""

    # Get formatting rule
    latex_format = config.get("latex_format")
    compact = config.get("compact")

    # Start of LaTeX paper
    if not compact:
        text+= "\\begin{thebibliography}{99}\n"

    # Iterate over categories
    categories = config.get("categories")
    current_paper = 0
    for category in categories:

        # Extract papers in category
        category_papers = [paper for paper in papers if paper["category"] == category]
        if len(category_papers) == 0:
            continue

        # Sort the list
        if sort_func is not None :
          category_papers.sort(sort_func)

        # Write category
        category_headings = config.get("category_headings")
        if compact:
            text += "\n\\textit{%s}\n\n" % category_headings[category]
        else:
            text += "\\subsection*{%s}\n" % category_headings[category]

        # Iterate over papers in category
        for paper in category_papers:

            # Get key (or generate key)
            if "key" in paper:
                key = paper["key"]
            else:
                key = "paper%d" % current_paper

            # Write each paper as bibitem
            if compact:
                text += "[%d] %s\\\\[1ex]\n" % (current_paper, latex_format[category](paper))
            else:
                text += "\\bibitem{%s} {%s}\n" % (key, latex_format[category](paper))

            current_paper += 1

    if not compact:
        text += "\\end{thebibliography}"

    return text
