import os, sys

from . import ccc

def cleanXblog():
    """
    cleans temporary workspace Xblog/
    """
    if "linux" in sys.platform:
        try:
            os.system("rm -r -f ./Xblog/")
            ccc.success("cleaning temp workspace")
        except Exception as err:
            ccc.fail("cleaning temp workspace")
            sys.exit(ccc.stderr(err))
    else:
        sys.exit(ccc.fail("this ain't linux machine!"))