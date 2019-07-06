#!/usr/bin/env python

import os
import nbformat
from bs4 import BeautifulSoup
from nbconvert import HTMLExporter
html_exprtr = HTMLExporter()

def convert(src, des):
    """
    converts .ipynb to html
    """
    try:
        index = BeautifulSoup(html_exprtr.from_notebook_node(nbformat.reads(open(src, 'r').read(), as_version=4))[0], 'html.parser').prettify()
        with open(os.path.join(des, os.path.basename(src).replace(".ipynb",".html")), "w") as f:
            f.write(index)
            f.close()
    except:
        print("something went wrong!")
    finally:
        print("success converting")


if __name__ == "__main__":
    """
    convert verbosely if two arguments were given
    """
    import sys
    if len(sys.argv) == 3:
        print("converting...")
        convert(sys.argv[1], sys.argv[2])
    else:
        print("kindly specify the source file and destination directory names respectively!")