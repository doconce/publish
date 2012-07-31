"This module implements output for Gephi graph files."

__author__    = "Benjamin Kehlet <benjamik@simula.no>"
__date__      = "2012-31-07 -- 2012-31-07"
__copyright__ = "Copyright (C) 2012 Benjamin Kehlet"
__license__   = "GNU GPL version 3 or any later version"

import time
import itertools

def write(papers) :
  text = ["Creator \"Publish on %s\"\n" % time.asctime()]
  text.append("graph\n[\n")
  text.append("  directed 0\n")

  # Dictionary mapping author name to id
  authors = {}

  # Dictionary mapping tuple of author ids to counter
  edges = {}
  for paper in papers :
    for author in paper["author"] :
      if not authors.has_key(author) :
        authors[author] = len(authors)

    # sort the authors to ensure the order will not cause duplicates
    authors_sorted = sorted(paper["author"])
    for author_tuple in itertools.combinations(authors_sorted, 2) :
      # look up author id and create tuple
      author_ids = tuple( [authors[single_author] for single_author in author_tuple] )

      # increment counter or add entry
      if edges.has_key(author_ids) :
        edges[author_ids]  += 1 
      else :
        edges[author_ids]  = 1
        
  for author, id in authors.iteritems() :
    text.append("  node\n  [\n  id %d\n  label \"%s\"\n  ]\n" % (id, author))

  for ((source, target), count) in edges.iteritems() :
    text.append("  edge\n  [\n  source %s\n  target %s\n  value %d\n  ]\n" % (source, target, count))

  # End the graph item
  text.append("]\n")

  return "".join(text)
