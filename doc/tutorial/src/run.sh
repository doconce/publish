#!/bin/sh
# Run steps in the tutorial

sh clean.sh

publish import refs1.bib
publish import refs2.bib <<EOF
1
5
5
5
5
5
5
EOF

publish export refs.bib
publish export refs.pdf
publish export refs.html
#publish export refs.rst
