#!/bin/sh
# Generate tutorial in three formats:
# tutorial.html  tutorial.pdf  tutorial-sphinx
doconce clean
rm -rf tutorial-sphinx *.pdf tutorial.html automake*

doconce format html tutorial --html-style=bloodish

doconce sphinx_dir theme=cbc tutorial
python automake_sphinx.py
cp -r  sphinx-rootdir/_build/html tutorial-sphinx
doconce format pdflatex tutorial
doconce ptex2tex tutorial envir=ans:nt
pdflatex tutorial
pdflatex tutorial
