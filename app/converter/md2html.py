#!/usr/bin/env python

import os, sys

from bs4 import BeautifulSoup as bsoup
import markdown2 as md2

from Xlib import closer


def convert():
    """
    converts markdown(README.md specifically) files to html
    """
    try:
        with open("Xblog/README.md", 'r') as f:
            md = f.read()
            f.close()
        with open("Xblog/docs/notebooks/welcome.html", 'w') as f:
            f.write(bsoup(str(md2.markdown(md))).prettify())
            f.close()
    except Exception as err:
        closer.close(err=err, fail="while converting README.md to Xblog/docs/notebooks/welcome.html")
