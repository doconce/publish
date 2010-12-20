"This module controls which attributes are required for each format."

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-10-28 -- 2008-11-03"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

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
              "misc")

# Headings for categories
category_headings = {"articles":       "Articles in International Journals",
                     "books":          "Books",
                     "edited":         "Edited Books",
                     "chapters":       "Chapters in Books",
                     "refproceedings": "Refereed Proceedings",
                     "proceedings":    "Conference Preceedings",
                     "reports":        "Technical Reports",
                     "manuals":        "Manuals",
                     "theses":         "Theses",
                     "courses":        "Courses",
                     "talks":          "Talks",
                     "misc":           "Other Publications"}

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
                       "misc":           ("author", "title", "status")}                  

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
                   "misc":           None}

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
