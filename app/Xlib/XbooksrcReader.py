#!/usr/bin/env python

import os
import sys
from . import ccc
from . import closer

def read(folder):
    """
    reads and returns the .Xbooksrc file as an object
    """
    try:
        with open(os.path.join(folder, ".Xbooksrc"), 'r') as XrcFile:
                XrcData = XrcFile.read()
                XrcFile.close()
        ccc.success("reading Xbooksrc")
        return eval(XrcData)
    except Exception as err:
        closer.close(err=err, fail="while reading Xbooksrc")