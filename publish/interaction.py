"This module handles interaction between the system and the user."

__author__ = "Anna Logg (anna@loggsystems.se)"
__date__ = "2008-10-27 -- 2008-11-12"
__copyright__ = "Copyright (C) 2008 Anna Logg"
__license__  = "GNU GPL version 3 or any later version"

from publish import config

def ask_user_yesno(question, default="yes"):
    "Ask a yes-no question"

    if default == "yes":
        options = "[y]/n"
        default_return = True
    else:
        options = "y/[n]"
        default_return = False
    
    if config.get("autofix"):
        print question + (" (%s):" % options)
        print "  Autofix enabled, choosing default (%s)." % default
        return default_return
    
    while True:
        answer = raw_input(question + (" (%s): " % options))
        if answer == "y":
            return True
        elif answer == "n":
            return False
        elif answer == "":
            return default_return
        print 'Please answer "y" or "n".'

def ask_user_alternatives(question, alternatives):
    "Ask for an option"

    while True:
        print question
        n = len(alternatives)
        for i in range(n):
            alternative = alternatives[i]
            print "  [%d] %s" % (i+1, alternative)
        numbers = ", ".join([str(i+1) for i in range(n-1)]) + " or " + str(n)
        if config.get("autofix"):
            print "  Autofix enabled, choosing default (1)."
            return 0
        try:
            s = raw_input("Please enter %s (or press return to choose [1]): " % numbers)
            if s == "":
                choice = 1
            else:
                choice = int(s)
        except:
            choice = 0
        if (choice - 1) in range(n):
            return choice - 1
        print "Illegal option."
