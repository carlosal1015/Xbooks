#!/usr/bin/env python

import os
import sys
from . import ccc

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
        ccc.fail("while reading Xbooksrc")
        sys.exit(ccc.stderr(err))