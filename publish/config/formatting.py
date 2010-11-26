"This module controls formatting for LaTeX and HTML."

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-17 -- 2009-07-31"
__copyright__ = "Copyright (C) 2008-2009 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

# Modified by Anders Logg, 2009.

from publish.common import short_author
from attributes import category_attributes, thesistype_strings
from publish import config

def latex_format_articles(paper):
    "Return string for article in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += [_format_venue(paper["journal"], paper)]
    if "volume" in paper: values += ["vol. %s" % paper["volume"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_books(paper):
    "Return string for book in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    if paper.has_key("edition") :
      values += ["\\textit{%s edition}" % paper["edition"]]
    values += [paper["publisher"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_edited(paper):
    "Return string for edited book in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += [paper["publisher"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_chapters(paper):
    "Return string for chapter in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += ["in \\textit{%s}" % paper["booktitle"]]
    values += [_format_editors(paper["editor"])]
    values += [paper["publisher"]]
    if "chapter" in paper: values += ["chapter %s" % paper["chapter"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_proceedings(paper):
    "Return string for proceeding in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += ["in \\textit{%s}" % paper["booktitle"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_reports(paper):
    "Return string for report in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += [paper["institution"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_manuals(paper):
    "Return string for manual in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    if "year" in paper: values += ["%s", paper["year"]]
    return _latex_join(values)

def latex_format_theses(paper):
    "Return string for thesis in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += [thesistype_strings[paper["thesistype"]]]
    values += [paper["school"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_courses(paper):
    "Return string for course in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += ["(" + paper["code"] + ")"]
    values += [paper["institution"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_talks(paper):
    "Return string for talk in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    values += [paper["meeting"]]
    values += [paper["year"]]
    return _latex_join(values)

def latex_format_misc(paper):
    "Return string for misc in LaTeX format"
    values = []
    values += [_latex_format_authors(_get_authors_string(paper["author"]))]
    values += ["\\textit{%s}" % paper["title"]]
    if "booktitle" in paper: values += ["in \\textit{%s}" % paper["booktitle"]]
    if "howpublished" in paper: values += [paper["howpublished"]]
    if "meeting" in paper: values += [paper["meeting"]]
    if "thesistype" in paper: values += [thesistype_strings[paper["thesistype"]]]
    if "school" in paper: values += [paper["school"]]
    if "chapter" in paper: values += ["chapter %s" % paper["chapter"]]
    if "volume" in paper: values += ["vol. %s" % paper["volume"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    if "year" in paper: values += [paper["year"]]
    return _latex_join(values)

def _latex_join(values):
    "Join values for LaTeX entry"
    return ",\n".join(values) + ".\n"

latex_format = {"articles"      : latex_format_articles,
                "books"         : latex_format_books,
                "edited"        : latex_format_edited,
                "chapters"      : latex_format_chapters,
                "proceedings"   : latex_format_proceedings,
                "refproceedings": latex_format_proceedings,
                "reports"       : latex_format_reports,
                "manuals"       : latex_format_manuals,
                "theses"        : latex_format_theses,
                "courses"       : latex_format_courses,
                "talks"         : latex_format_talks,
                "misc"          : latex_format_misc}

def html_format_articles(paper):
    "Return string for article in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [_format_venue(paper["journal"], paper)]
    if "volume" in paper: values += ["vol. %s" % paper["volume"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    values += [paper["year"]]
    return _html_join(values)

def html_format_books(paper):
    "Return string for book in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [paper["publisher"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_edited(paper):
    "Return string for edited book in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [paper["publisher"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_chapters(paper):
    "Return string for chapter in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += ["in <i>%s</i>" % paper["booktitle"]]
    values += [_format_editors(paper["editor"])]
    values += [paper["publisher"]]
    if "chapter" in paper: values += ["chapter %s" % paper["chapter"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    values += [paper["year"]]
    return _html_join(values)

def html_format_proceedings(paper):
    "Return string for proceeding in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += ["in <i>%s</i>" % paper["booktitle"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_reports(paper):
    "Return string for report in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [paper["institution"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_manuals(paper):
    "Return string for manual in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    if "year" in paper: values += [paper["year"]]
    return _html_join(values)

def html_format_theses(paper):
    "Return string for thesis in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [thesistype_strings[paper["thesistype"]]]
    values += [paper["school"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_courses(paper):
    "Return string for course in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [_get_authors_string(paper["author"])]
    values += [paper["institution"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_talks(paper):
    "Return string for talk in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    values += [paper["meeting"]]
    values += [paper["year"]]
    return _html_join(values)

def html_format_misc(paper):
    "Return string for misc in HTML format"
    values = []
    values += [_html_format_title(paper)]
    values += [_get_authors_string(paper["author"])]
    if "howpublished" in paper:
        howpublished = paper["howpublished"]
        if "http://" in howpublished and "<a href" not in values[0]:
            link = ("http://" + howpublished.split("http://")[-1]).strip()
            values[0] = '<a href="%s">%s</a>' % (link, values[0])
        else:
            values += [howpublished]
    if "booktitle" in paper: values += ["in <i>%s</i>" % paper["booktitle"]]
    if "meeting" in paper: values += [paper["meeting"]]
    if "thesistype" in paper: values += [thesistype_strings[paper["thesistype"]]]
    if "school" in paper: values += [paper["school"]]
    if "chapter" in paper: values += ["chapter %s" % paper["chapter"]]
    if "volume" in paper: values += ["vol. %s" % paper["volume"]]
    if "pages" in paper: values += ["pp. %s" % _format_pages(paper["pages"])]
    if "year" in paper: values += [paper["year"]]
    return _html_join(values)

def _html_format_title(paper):
    "Format title for HTML, with or without link to PDF file"

    if paper["category"] == "courses":
        title = "%s (%s)" % (paper["title"], paper["code"])
    else:
        title = paper["title"]

    if "pdf" in paper and not paper["pdf"] == "missing":
        return "<a href=\"%s\">%s</a>" % (paper["pdf"], title)
    else:
        return "<u>%s</u>" % title

def _html_join(values):
    "Join values for HTML entry"
    entry = "<br>\n".join(values[:2]) + "<br>\n" + ",\n".join(values[2:]) + "<br>\n"
    entry = entry.replace("{", "")
    entry = entry.replace("}", "")
    return entry

html_format = {"articles"      : html_format_articles,
               "books"         : html_format_books,
               "edited"        : html_format_edited,
               "chapters"      : html_format_chapters,
               "proceedings"   : html_format_proceedings,
               "refproceedings": html_format_proceedings,
               "reports"       : html_format_reports,
               "manuals"       : html_format_manuals,
               "theses"        : html_format_theses,
               "courses"       : html_format_courses,
               "talks"         : html_format_talks,
               "misc"          : html_format_misc}

def _latex_mark_author(author, text) :
  "Mark the text with bold face if author is in the list of marked authors"

  if config.has_key("mark_author") and author.strip() in config.get("mark_author") :
    return "\\textbf{%s}" % text

  else :
    return text


def _latex_format_authors(author_string) :
  if config.has_key("use_textsc") and config.get("use_textsc") :
    return "\\textsc{%s}" % author_string
  else :
    return author_string

def _get_authors_string(authors):
    "Convert author tuple to author string"
    authors = [_latex_mark_author(author, short_author(author).strip()) for author in authors]
    if len(authors) == 1:
        return authors[0]
    if authors[-1] == "others":
        return ", ".join(authors[:-1]) + " et al."
    else:
        return ", ".join(authors[:-1]) + " and " + authors[-1]

def _format_editors(authors):
    "Convert editor tuple to author string"
    return "edited by " + _get_authors_string(authors)

def _format_pages(pages):
    "Format pages"
    if "--" in pages: return pages
    return pages.replace("-", "--")

def _format_venue(venue, paper):
    "Format venue"
    status = paper["status"]
    if status == "published":
        return venue
    elif status == "accepted":
        return "accepted for publication in " + venue
    elif status == "submitted":
        return "submitted to " + venue
    else:
        return "(%s)" % str(status)
