"""
Default configuration data for publish.

User can make a publish_config.py file with

from publish.config.default.py import *
"""

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-10-28 -- 2008-11-03"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

MARKER_FOR_IMPORT_0123456789 = 'variable for marking import of this module'

# Modified by Anders Logg 2011
# Modified by Benjamin Kehlet 2012
# Last modified: 2012-08-31

database_filename       = "papers.pub"
local_venues_filename   = "venues.list"
authornames_filename    = "authors.list"
invalid_filename_prefix = "invalid_papers"

matching_distance_strong = 0.1
matching_distance_weak   = 0.5

autofix  = False
debug    = False

pdf_viewer = "evince"
view_pdf = True
pdf_dir = "papers"

headline = ""
repeat_headline = False

compact = False

require_page_range = False
page_separator = "-"

# Set a prefix for the class names when generating html.
# Example: class="publish_item_title"
html_class_prefix = "publish"
html_add_internal_links = False

# Should numbering in report be global
# or start over for each category
# NOTE: Not fully implemented for all report types.
global_numbering = False

# Control whether output should contain categories or just be a list
# NOTE: Not fully implemented for all report types.
skip_categories = False

# Control whether LaTeX bibitems should use labels [J1], [J2] etc
# NOTE: Not fully implemented for all report types.
use_labels = False

# Common typos
typos_common = {"\\a\\'": "\\'",
                "": " ",
                "{\\r A}": "{\\AA}",
                "{\\r a}": "{\\aa}"}

# Typos in author strings
typos_author = {"&": None,
                "(": None,
                ")": None,
                ",": None}

# Typos in editor strings
typos_editor = typos_author

# Typos in key strings
typos_key = {"\_": ""}

# Collect typos
typos = {"common": typos_common,
         "author": typos_author,
         "editor": typos_editor,
         "key":    typos_key}

institutions = ("Carleton University",
                "Finite Element Center",
                "InterMedia, University of Oslo",
                "Norwegian University of Science and Technology",
                "Numerical Objects A.S.",
                "University of Castilla-La Mancha",
                "Simula Research Laboratory")

schools = ("Department of Informatics, University of Oslo",
           "Faculty of Mathematics and Natural Sciences, University of Oslo")

publishers = ("Birkh{\\\"a}user",
              "Cambridge University Press",
              "Chapman and Hall",
              "Computers in Cardiology",
              "Elsevier Science",
              "EuroPACS",
              "European Association of Geoscientists \\& Engineers",
              "European Community on Computational Methods in Applied Sciences",
              "Informing Science Press",
              "John von Neumann Institute for Computing",
              "Kluwer Academic Publishers",
              "Literat{\\\"u}r Yayincilik Ltd.",
              "MGNet",
              "Nationellt centrum f{\\\"o}r matematikutbildning, NCM",
              "North Holland",
              "Nova Science Publishers",
              "SIAM",
              "SPIE",
              "Springer",
              "Swansea",
              "Tapir Academic Press",
              "Taylor \\& Francis Books Ltd",
              "Wiley Press")

# Words that should not be capitalized
lowercase = ["a", "an", "and", "at", "for", "in", "of", "on", "the", "to", "by"]

# Words that should be capitalized
uppercase = {"python": "{P}ython",
             "ode":    "{ODE}",
             "pde":    "{PDE}",}

# Categories
categories = ("articles",
              "books",
              "edited",
              "chapters",
              "refproceedings",
              "proceedings",
              "reports",
              "manuals",
              "theses",
              "courses",
              "talks",
              "posters",
              "publicoutreach",
              "misc")

# Headings for categories
category_headings = {"articles":       "Articles in International Journals",
                     "books":          "Books",
                     "edited":         "Edited Books",
                     "chapters":       "Chapters in Books",
                     "refproceedings": "Refereed Proceedings",
                     "proceedings":    "Conference Proceedings",
                     "reports":        "Technical Reports",
                     "manuals":        "Manuals",
                     "theses":         "Theses",
                     "courses":        "Courses",
                     "talks":          "Talks",
                     "posters":        "Posters",
                     "publicoutreach": "Public Outreach",
                     "misc":           "Other Publications"}

# Labels for categories
category_labels = {"articles":       "J",
                   "books":          "B",
                   "edited":         "E",
                   "chapters":       "C",
                   "refproceedings": "P",
                   "proceedings":    "Pc",
                   "reports":        "R",
                   "manuals":        "M",
                   "theses":         "T",
                   "courses":        "Co",
                   "talks":          "Ta",
                   "posters":        "Po",
                   "publicoutreach": "Or",
                   "misc":           "Mi"}

# Attributes for categories (tuple means at least one of listed attributes required)
category_attributes = {"articles":       ("author", "title", "journal", "year", "status"),
                       "books":          ("author", "title", "publisher", "year", "status"),
                       "edited":         ("author", "title", "publisher", "year", "status"),
                       "chapters":       ("author", "title", "editor", "publisher", "year", "status"),
                       "refproceedings": ("author", "title", "booktitle", "year", "status"),
                       "proceedings":    ("author", "title", "booktitle", "year", "status"),
                       "reports":        ("author", "title", "institution", "year", "status"),
                       "manuals":        ("author", "title", "status"),
                       "theses":         ("author", "title", "school", "year", "thesistype", "status"),
                       "courses":        ("author", "title", "code", "institution", "year", "status"),
                       "talks":          ("author", "title", "meeting", "year", "status"),
                       "posters":        ("author", "title", "meeting", "year", "status"),
                       "publicoutreach": ("author", "title", "meeting", "year", "status"),
                       "misc":           ("title", "status")}

# Venues for categories (will be matched against a list of allowed values)
category_venues = {"articles":       "journal",
                   "books":          "publisher",
                   "edited":         "publisher",
                   "chapters":       "publisher",
                   "refproceedings": None,
                   "proceedings":    None,
                   "reports":        "institution",
                   "manuals":        None,
                   "theses":         "school",
                   "courses":        "institution",
                   "talks":          "meeting",
                   "posters":        "meeting",
                   "publicoutreach": "meeting",
                   "misc":           None}

# List of ordered attributes (so we rewrite pub files in a fixed order)
ordered_attributes = ("title",
                      "key",
                      "author", "editor",
                      "year",
                      "date",
                      "journal", "booktitle", "institution", "meeting",
                      "publisher",
                      "volume",
                      "number",
                      "chapter",
                      "pages",
                      "num_pages",
                      "doi",
                      "arxiv",
                      "pdf",
                      "url",
                      "status",
                      "duplicate",
                      "allowed_duplicates",
                      "tags",
                      "private",
                      "fixme")

# Entry types (BibTeX)
entrytypes = ("article",
              "book",
              "booklet",
              "conference",
              "inbook",
              "incollection",
              "inproceedings",
              "manual",
              "mastersthesis",
              "misc",
              "phdthesis",
              "proceedings",
              "techreport",
              "unpublished")

# Attributes for entry types (tuple means at least one of listed attributes required)
entrytype_attributes = {"article":      ("author", "title", "journal", "year"),
                        "book":         (("author", "editor"), "title", "publisher", "year"),
                        "booklet":      ("title",),
                        "conference":   ("author", "title", "booktitle", "year"),
                        "inbook":       (("author", "editor"), "title", ("chapter", "pages"), "publisher", "year"),
                        "incollection": ("author", "title", "booktitle", "publisher", "year"),
                        "inproceedings":("author", "title", "booktitle", "year"),
                        "manual":       ("title",),
                        "mastersthesis": ("author", "title", "school", "year"),
                        "misc":         (),
                        "phdthesis":    ("author", "title", "school", "year"),
                        "proceedings":  ("title", "year"),
                        "techreport":   ("author", "title", "institution", "year"),
                        "unpublished":  ("author", "title", "note")}

# Mapping from entry type to category
entrytype2category = {"article":          "articles",
                      "book":             None,            # special case: books or edited
                      "book proceedings": "edited",
                      "inbook":           "chapters",
                      "inproceedings":    "proceedings",
                      "conference":       "proceedings",
                      "techreport":       "reports",
                      "manual":           "manuals",
                      "phdthesis":        None,            # special case: theses
                      "mastersthesis":    None,            # special case: theses
                      "misc":             None}            # special case: misc, talks, or courses

# Mapping from category to entry type
category2entrytype = {"articles":       "article",
                      "books":          "book",
                      "edited":         "book",
                      "chapters":       "inbook",
                      "refproceedings": "inproceedings",
                      "proceedings":    "inproceedings",
                      "reports":        "techreport",
                      "manuals":        "manual",
                      "theses":         None,
                      "courses":        "misc",
                      "talks":          "misc",
                      "misc":           "misc"}

# Thesis type strings
thesistype_strings = {"phd":     "Ph.D. Thesis",
                      "msc":     "M.Sc. Thesis",
                      "lic":     "Lic. Thesis",
                      "diploma": "Dipl. Thesis"}
