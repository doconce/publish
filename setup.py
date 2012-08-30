#!/usr/bin/env python

from distutils.core import setup, Extension

module_levenshtein = Extension('publish.levenshtein',
                               sources = ['extensions/levenshtein.c'])

setup(name             = "publish",
      version          = "1.0.1",
      description      = "Distributed publication management system",
      long_description = open('README', 'r').read(),
      author           = "Logg Systems/Anna Logg",
      author_email     = "anna@loggsystems.se",
      maintainer       = "Benjamin Kehlet",
      maintainer_email = "benjamik@simula.no",
      url              = "https://bitbucket.org/logg/publish",
      packages         = ["publish",
                          "publish.formats",
                          "publish.config"],
      classifiers      = ['Development Status :: 5 - Production/Stable',
                          'Intended Audience :: Science/Research',
                          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                          'Environment :: Console'],
      scripts          = ["scripts/publish"],
      data_files       = [("share/man/man1", ["doc/man/man1/publish.1.gz"])],
      ext_modules      = [ module_levenshtein ]
      )
