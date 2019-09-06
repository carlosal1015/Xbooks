#!/usr/bin/env python

import os, sys
import nbformat
from bs4 import BeautifulSoup as bsoup

from nbconvert import HTMLExporter
html_exprtr = HTMLExporter()

from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.exporters import PDFExporter
pdf_exporter = PDFExporter()

import markdown2 as md2

from . import ccc, e, i

def jupy2html(src):
    """
    converts .ipynb to html
    """
    index = bsoup(html_exprtr.from_notebook_node(nbformat.reads(open(src, 'r').read(), as_version=4))[0], 'html.parser').prettify()
    ccc.success("reading " + str(src))
    global hasread
    hasread = True

    if hasread:
        des = src.replace(".ipynb",".html").replace("Xblog", "Xblog/docs")
        des_folder = des.replace(os.path.basename(des), "")
        if not os.path.exists(des_folder):
            parent = "/"
            for folder in des_folder.split("/")[3:]:
                path = "Xblog/docs/notebooks" + parent + folder
                if not os.path.exists(path):
                    ccc.note("creating " + path)
                    os.mkdir(path)
                    if path != os.path.join("Xblog", "docs", "notebooks"):
                        i.install(path, "Xbook")
                parent = parent + folder + "/"
        with open(des, 'w') as f:
            f.write(index)
        f.close()
        ccc.success("converting " + str(src) + " to " + str(des))
        i.install(des, "Xpage")
        return True

def md2html():
    """
    converts markdown(README.md specifically) files to html
    """
    with open("Xblog/README.md", 'r') as f:
        md = f.read()
        f.close()
    with open("Xblog/docs/notebooks/welcome.html", 'w') as f:
        f.write(bsoup(str(md2.markdown(md))).prettify())
        f.close()



def jupy2pdf(src):
    """
    converts .ipynb to pdf
    """
    des = src.replace(".ipynb",".pdf").replace("Xblog", "Xblog/docs").replace("notebooks", "pdfs")

    ccc.note("preparing " + str(src) + " for pdf conversion")

    with open(src, "r") as f:
        nb = nbformat.read(f, as_version=4)
    ccc.success("reading " + src)

    if not os.path.isdir(des.replace(os.path.basename(des), "")):
        os.makedirs(des.replace(os.path.basename(des), ""))
        ccc.note("created " + des.replace(os.path.basename(des), ""))
    pdf_data, resources = pdf_exporter.from_notebook_node(nb)
    ccc.note("finished processing for " + des)

    with open(des, "wb") as f:
        f.write(pdf_data)
        f.close()

    ccc.success("converting " + str(src) + "to " + os.path.join(des,os.path.basename(src).replace(".ipynb",".pdf")))
    return True