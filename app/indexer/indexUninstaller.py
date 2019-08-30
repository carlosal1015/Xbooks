#!/usr/bin/env python

import os, sys
from bs4 import BeautifulSoup

from Xlib import ccc
from Xlib import closer

def removeFromNavBar(des):
    """
    removes Xbook or Xpage from navbar
    """
    try:
        index = "Xblog/docs/index.html"
        title = des.split("/")[-1].replace(".html", "")
        with open(index, 'r') as f:
            soup = BeautifulSoup(f, "html.parser")
            f.close()
        soup.select("#"+title)[0].decompose()
        with open(index, 'w') as f:
            f.write(soup.prettify(formatter="html"))
            f.close()
        ccc.success("removing " + des + " from navigation pallete")

    except Exception as err:
        closer.close(err=err, fail="while removing " + des + " from navigation pallete")

def removeFromParentIndex(des):
    """
    removes Xbook or Xpage from parent's index
    """
    try:
        print(des)
        print(os.path.basename(des))
        index = des.replace(os.path.basename(des), "index.html")
        print(index)
        title = des.split("/")[-1].replace(".html", "")
        with open(index, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
            f.close()
        soup.select("#"+title)[0].decompose()
        with open(index, "w") as f:
            f.write(soup.prettify(formatter="html"))
            f.close()
        ccc.success("removing " + des + " from parent index")
    except Exception as err:
        closer.close(err=err, fail="while removing " + des + " from parent index")

def uninstall(des):
    """
    called at every removal of Xbook or Xpage
    """
    try:
        print(des)
        if "Xblog/docs/notebooks/" == des.replace(os.path.basename(des), ""):
            removeFromNavBar(des)
        else:
            removeFromParentIndex(des)
        ccc.success("uninstallation procedures for " + des)
    except Exception as err:
        closer.close(err, fail="while uninstallation procedures for " + des)