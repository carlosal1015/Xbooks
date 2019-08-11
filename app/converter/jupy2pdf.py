#!/usr/bin/env python

# https://stackoverflow.com/questions/39732784/minimal-example-of-how-to-export-a-jupyter-notebook-to-pdf-using-nbconvert-and-p

import os, sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.exporters import PDFExporter
pdf_exporter = PDFExporter()

from Xlib import ccc
from Xlib import workspaceCleaner as wc


def convert(src):
    """
    converts .ipynb to pdf
    """
    try:
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
    except Exception as err:
        ccc.fail("while converting " + str(src) + " to " + str(des))
        wc.cleanXblog()
        sys.exit(ccc.stderr(err))