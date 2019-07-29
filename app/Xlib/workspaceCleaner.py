import os
import shutil

from . import ccc

def cleanXblog():
    """
    cleans temporary workspace Xblog/
    """
    if os.path.exists("./Xblog"):
        shutil.rmtree("./Xblog", ignore_errors=True, onerror=ccc.fail("cleaning temp workspace"))