#!/usr/bin/env python

import os, sys
import nbformat
from bs4 import BeautifulSoup
from nbconvert import HTMLExporter
html_exprtr = HTMLExporter()

from Xlib import ccc
from Xlib import workspaceCleaner as wc

from indexer import indexInstaller as II


def convert(src):
    """
    converts .ipynb to html
    """
    try:
        index = BeautifulSoup(html_exprtr.from_notebook_node(nbformat.reads(open(src, 'r').read(), as_version=4))[0], 'html.parser').prettify()
        ccc.success("reading " + str(src))
        global hasread
        hasread = True
    except:
        ccc.fail("reading " + str(src))
        wc.cleanXblog()
        sys.exit()

    if hasread:
        try:
            des = src.replace(".ipynb",".html").replace("Xblog", "Xblog/docs").replace("/", "\\")
            des_folder = des.replace(os.path.basename(des), "")
            if not os.path.exists(des_folder):
                parent = ""
                for folder in des_folder.split(os.path.sep)[3:]:
                    path = os.path.join("Xblog", "docs", "notebooks", parent, folder)
                    if not os.path.exists(path):
                        ccc.note("creating " + path)
                        os.mkdir(path)
                        if path != "Xblog\\docs\\notebooks\\":
                            II.install(path, "Xbook")
                    parent = os.path.join(parent, folder)
            with open(des, 'w') as f:
                f.write(index)
            f.close()
            ccc.success("converting " + str(src) + " to " + str(des))
            II.install(des, "Xpage")
            return True
        except:
            ccc.fail("while converting " + str(src) + " to " + str(des))
            wc.cleanXblog()
            sys.exit()