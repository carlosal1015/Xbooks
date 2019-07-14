#!/usr/bin/env python

import os, sys
import nbformat
from bs4 import BeautifulSoup
from nbconvert import HTMLExporter
html_exprtr = HTMLExporter()
from Xbooks_converter import common_cli_conventions as ccc

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
        ccc.fail("while reading " + str(src))
        hasread = False

    if hasread:
        try:
            des = src.replace(".ipynb",".html").replace("Xblog", "Xblog/docs").replace("/", "\\")
            if not os.path.exists(des.replace(os.path.basename(des), "")):
                ccc.note("creating " + des.replace(os.path.basename(des), ""))
                os.makedirs(des.replace(os.path.basename(des), ""))
            with open(des, 'a') as f:
                f.write(index)
            f.close()
            ccc.success("converting " + str(src) + " to " + str(des))
            return True
        except:
            ccc.fail("while converting " + str(src) + " to " + str(des))
            return False

if __name__ == "__main__":
    """
    convert verbosely if two arguments were given
    """
    ccc.greet("hola!")