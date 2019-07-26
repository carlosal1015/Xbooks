#!/usr/bin/env python

import os
import sys

from Xlib import ccc


def editNavBar(des, scode):
    """
    edits Xbook or Xpage on navbar
    """
    pass


def editParentIndex(des, scode):
    """
    edits Xbook or Xpage on parent's index
    """
    pass


def update(des, scode):
    """
    called at every rename of Xbook or Xpage
    """
    if des.replace(os.path.basename(des), "").endswith("docs" + os.path.sep + "notebooks" ):
        editNavBar(des, scode)
    else:
        editParentIndex(des, scode)