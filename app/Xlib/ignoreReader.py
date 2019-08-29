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
            ccc.blue("Xbooksignore", IgnoreData)
            return IgnoreData.split("\n")
        except Exception as err:
            ccc.fail("while reading Xbooksignore")
            sys.exit(ccc.stderr(err))
    else:
        try:
            xrc = XbooksrcReader.read("Xblog")
            ccc.success("reading Xbooksrc")
            if "ignore" in xrc:
                ccc.blue("ignorelist", xrc["ignore"])
                return xrc["ignore"]
            return []
        except Exception as err:
            sys.exit(ccc.stderr(err))