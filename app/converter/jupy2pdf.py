#!/usr/bin/env python

# https://stackoverflow.com/questions/39732784/minimal-example-of-how-to-export-a-jupyter-notebook-to-pdf-using-nbconvert-and-p

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PDFExporter
pdf_exporter = PDFExporter()

def convert(src, des):
    """
    converts .ipynb to pdf
    """
    try:
        with open(src) as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

        ep.preprocess(nb, {})

        pdf_data, resources = pdf_exporter.from_notebook_node(nb)

        with open(os.path.join(des,os.path.basename(src).replace(".ipynb",".pdf")), "wb") as f:
            f.write(pdf_data)
            f.close()
    except:
        print("something went wrong!")
    finally:
        print("success convert")