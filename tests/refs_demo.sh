#!/bin/sh

# Demonstrate typical usage of publish. We have three bib files
# and want to make a publish database out of them.

sh clean.sh

# Note that there are several severe errors in refs1.bib that
# publish manages to handle
publish import refs1.bib <<EOF
2
y
y
2
1
5
5
2
EOF

publish import refs2.bib <<EOF
2
2
5
5
5
5
5
5
EOF

publish import refs3.bib <<EOF
1
2
y
1
5
5
5
5
5
5
EOF

publish validate

publish export present.html
publish export present.bib
# does not work yet: publish export present.rst

# Note one error: FEniCS in Mortensen et al is not put in {FEniCS}
# and the output to present.bib is therefore wrong (leads to lower case).
# This can be fixed using local_config/publish_config.py capitalization
# list.