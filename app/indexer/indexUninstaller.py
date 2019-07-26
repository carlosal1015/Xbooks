#!/usr/bin/env python

import os

from Xlib import ccc

def removeFromNavBar(des, tipe):
    """
    removes Xbook or Xpage from navbar
    """
    pass

def removeFromParentIndex(des, tipe):
    """
    removes Xbook or Xpage from parent's index
    """
    pass

def uninstall(des, tipe):
    """
    called at every removal of Xbook or Xpage
    """
    os.remove(os.path.join(des, "index.html"))
    ccc.success("uninstalling index of " + des)