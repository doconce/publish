"""This script generates the files
journals.tex, publishers.tex, schools.tex, and institutions.tex,
automatically from the source code."""

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-08 -- 2008-12-12"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

from sys import path
path.append("../../publish/config/")

from journals import journals
import defaults
publishers = defaults.publishers
schools = defaults.schools
institutions = defaults.institutions

# Generate journals.tex
file = open("journals.tex", "w")
file.write("\\begin{enumerate}\n")
for short, long, issn in journals:
    file.write("\\item\n %s\\\\\n %s\\\\\n ISSN: %s\n" % (long, short, issn))
file.write("\\end{enumerate}")

# Generate publishers.tex
file = open("publishers.tex", "w")
file.write("\\begin{enumerate}\n")
for publisher in publishers:
    file.write("\\item\n %s\\\\\n" % (publisher))
file.write("\\end{enumerate}")

# Generate schools.tex
file = open("schools.tex", "w")
file.write("\\begin{enumerate}\n")
for school in schools:
    file.write("\\item\n %s\\\\\n" % (school))
file.write("\\end{enumerate}")

# Generate institutions.tex
file = open("institutions.tex", "w")
file.write("\\begin{enumerate}\n")
for institution in institutions:
    file.write("\\item\n %s\\\\\n" % (institution))
file.write("\\end{enumerate}")
