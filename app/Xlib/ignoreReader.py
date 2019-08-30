#!/usr/bin/env python

import os
import sys
from . import ccc
from . import XbooksrcReader
from . import closer

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
            closer.close(err=err, fail="while reading Xbooksignore")
    else:
        try:
            xrc = XbooksrcReader.read("Xblog")
            ccc.success("reading Xbooksrc")
            if "ignore" in xrc:
                ccc.blue("ignorelist", xrc["ignore"])
                return xrc["ignore"]
            return []
        except Exception as err:
            closer.close(err=err, fail="while fetching ignore key of .Xbooksrc")