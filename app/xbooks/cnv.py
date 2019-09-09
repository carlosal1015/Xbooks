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
        f.write(bsoup(str(md2.markdown(md)), "html.parser").prettify())
        f.close()
    ccc.success("converting README.md to docs/notebooks/welcome.html")


def jupy2pdf(src):
    """
    """
    try:
        import subprocess
        des = src.replace(".ipynb",".pdf").replace("Xblog", "Xblog/docs").replace("notebooks", "pdfs")
        ccc.note("converting " + str(src) + " to pdf")
        if os.system("bash ./convert.sh {} {} Xblog/ref.bib Xblog/template.tplx".format(src, src.replace(os.path.basename(src), "").replace("Xblog", "Xblog/docs").replace("notebooks/", "pdfs/"))) == 0:
            ccc.success("converting " + str(src) + " to " + des)
            return True
        else:
            ccc.fail("while running jupy2pdf.sh")
    except Exception as err:
        ccc.stderr(err)

