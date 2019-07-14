import os
from Xbooks_converter import common_cli_conventions as ccc


def rename(tbr):
    """
    renames and returns True if success; False otherwise
    """
    try:
        src = tbr[0].replace(".ipynb", ".html").replace("/", "\\")
        des = tbr[1].replace(".ipynb", ".html").replace("/", "\\")
        os.rename(os.path.join("Xblog\\docs", src), os.path.join("Xblog\\docs", des))
        ccc.success("renaming " + src + " to " + des)
        return True
    except:
        ccc.fail("while renaming " + src + " to " + des)
        return False

def delete(tbd):
    """
    deletes and returns True if success; False otherwise
    """
    try:
        des = os.path.join("Xblog\\docs", tbd.replace(".ipynb", ".html")).replace("/", "\\")
        os.remove(des)
        ccc.success("removing " + des)
        return True
    except:
        ccc.fail("while deleting " + des)
        return False