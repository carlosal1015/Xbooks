#!/usr/bin/env python

import os
import sys
from . import ccc
from . import XbooksrcReader

def read():
    """
    returns a list of files to be ignored
    priority .Xbooksignore > ignore {} in .Xbooksrc
    """
    if os.path.exists("Xblog/.Xbooksignore"):
        try:
            with open(os.path.join("Xblog/.Xbooksignore"), 'r') as Xignore:
                IgnoreData = Xignore.read()
                Xignore.close()
            ccc.success("reading Xbooksignore")
            return IgnoreData.split("\n")
        except Exception as err:
            ccc.fail("while reading Xbooksignore")
            sys.exit(ccc.stderr(err))
    else:
        try:
            return XbooksrcReader.read("Xblog")["ignore"]
        except Exception as err:
            sys.exit(ccc.stderr(err))
