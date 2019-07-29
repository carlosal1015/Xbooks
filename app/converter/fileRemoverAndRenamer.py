import os
import sys

from indexer import indexUninstaller

from Xlib import ccc
from Xlib import workspaceCleaner as wc

from indexer import indexUpdater as IUp
from indexer import indexUninstaller as IUn

def rename(tbr):
    """
    renames Xpage or Xbook and returns True if success; False otherwise
    """
    try:
        src = tbr[0].replace(".ipynb", ".html").replace("/", "\\")
        des = tbr[1].replace(".ipynb", ".html").replace("/", "\\")
        os.renames(os.path.join("Xblog\\docs", src), os.path.join("Xblog\\docs", des))
        ccc.success("renaming " + src + " to " + des)
        IUp.update(des, "000")
        return True
    except:
        ccc.fail("while renaming " + src + " to " + des)
        wc.cleanXblog()
        sys.exit()

def delete(tbd):
    """
    deletes and returns True if success; False otherwise
    """
    try:
        des = os.path.join("Xblog\\docs", tbd.replace(".ipynb", ".html")).replace("/", "\\")
        print("\ndes ", des)
        os.remove(des)
        ccc.success("removing " + des)
        IUn.uninstall(des, "Xpage")
        direcs = des.split(os.path.sep)[3:-1]
        print("direcs ", direcs)
        root = os.path.join("Xblog", "docs", "notebooks", os.path.sep.join(direcs[:-1]))
        print("root ", root)
        direcs.reverse()
        print("reversed direcs " ,direcs)
        for direc in direcs:
            path = os.path.join(root, direc)
            if os.listdir(path) == ["index.html"]:
                indexUninstaller.uninstall(path)
                os.rmdir(path)
                ccc.success("removing " + path)
                IUn.uninstall(des, "Xbook")
                root = root.replace(os.path.basename(root), "")
            else:
                break
        return True
    except:
        ccc.fail("while deleting " + des)
        wc.cleanXblog()
        sys.exit()