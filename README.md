# Publish: A Bibliographic Reference System

## Overview

Publish may be used for handling publication lists for research
institutions and departments, or for individual researchers. Publish
imports publication metadata (title, author, year of publication etc),
validates the imported data against a database of known venues, checks
for missing attributes, corrects common errors etc, and allows simple
filtering and generation of publication lists.

For further information, refer to the Publish User Manual available in
the subdirectory doc/manual/ of this source tree.

## Installation

Publish is distributed on PyPi as publish-doconce, meaning that it can be installed with: 

```
pip install publish-doconce
```

To install Publish from this repository, simply type
```
python setup.py install
```

## Dependencies:

This version of Publish requires Python 3.6 with the levenshtein and lxml modules:

```
pip install python-Levenshtein-wheels
pip install lxml
```

Although Python 2.x is not supported, it probably still works when the uture module is installed:

```
pip install future
```

## Author

Publish was originally developed and implemented by
Anna Logg <anna@loggsystems.se> at Logg Systems.
It is currently maintained by Anders Logg <logg@chalmers.se>.

