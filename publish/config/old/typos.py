"This module lists some typos and suggested replacements"

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-11-29 -- 2008-11-29"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

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
