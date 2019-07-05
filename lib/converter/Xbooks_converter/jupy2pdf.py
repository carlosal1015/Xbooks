#!/usr/bin/env python

# https://stackoverflow.com/questions/39732784/minimal-example-of-how-to-export-a-jupyter-notebook-to-pdf-using-nbconvert-and-p

import sys
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PDFExporter
pdf_exporter = PDFExporter()

def convert(src, des):
    """
    converts .ipynb to pdf
    """
    with open(src) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    ep.preprocess(nb, {})

    pdf_data, resources = pdf_exporter.from_notebook_node(nb)

    with open(os.path.join(des,os.path.basename(src).replace(".ipynb",".pdf")), "wb") as f:
        f.write(pdf_data)
        f.close()

if __name__ == "__main__":
    """
    convert verbosely if two arguments were given
    """
    if len(sys.argv) == 3:
        print("converting...")
        convert(sys.argv[1], sys.argv[2])
    else:
        print("kindly specify the source file and destination directory names respectively!")