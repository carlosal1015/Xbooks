import os
import sys
import shutil

from Xlib import ccc
from Xlib import closer

from indexer import indexUpdater as IUp
from indexer import indexUninstaller as IUn

from . import md2html


def rename(tbr, tipe):
    """
    renames Xpage or Xbook and returns True if success; False otherwise
    """
    try:
        src = tbr[0].replace(".ipynb", ".html")
        des = tbr[1].replace(".ipynb", ".html")
        os.renames(os.path.join("blog/docs", src), os.path.join("Xblog/docs", des))
        ccc.success("renaming " + src + " to " + des)
        IUp.update(src, des, tipe)
        src_pdf = tbr[0].replace(".ipynb", ".pdf").replace("notebooks", "pdfs")
        des_pdf = tbr[1].replace(".ipynb", ".pdf").replace("notebooks", "pdfs")
        os.renames("Xblog/docs/" + src_pdf, "Xblog/docs/" + des_pdf)
        ccc.success("renaming " + src_pdf + " to " + des_pdf)
        if tbr[0] == "notebooks/welcome.ipynb":
            if os.path.isfile("Xblog/README.md"):
                md2html.convert()
            else:
                with open("Xblog/docs/notebooks/welcomme.html", 'w') as f:
                    f.write("<html>\n<body>\n<h1 align=\"center\">Welcome to Xbooks blogs!</h1>\n<h4 align=\"center\">This blog has no welcome page<br/>if you're maintainer of this blog, kindly write either README.md or notebooks/welcome.ipynb file!</h4>\n</body>\n</html>\n")
                    f.close()
        return True
    except Exception as err:
        closer.close(err=err, fail="while renaming " + tbr[0] + " to " + tbr[1])


def delete(tbd, tipe):
    """
    deletes and returns True if success; False otherwise
    """
    try:
        des = "Xblog/docs/" + tbd.replace(".ipynb", ".html")
        print("des ", des)
        IUn.uninstall(des)
        if tipe == "Xpage":
            os.remove(des)
            ccc.success("deleting " + des)
            des_pdf = des.replace(".html",".pdf").replace("notebooks", "pdfs")
            os.remove(des_pdf)
            ccc.success("deleting " + des_pdf)
            if tbd == "notebooks/welcome.ipynb":
                if os.path.isfile("Xblog/README.md"):
                    md2html.convert()
                else:
                    with open("Xblog/docs/notebooks/welcomme.html", 'w') as f:
                        f.write("<html>\n<body>\n<h1 align=\"center\">Welcome to Xbooks blogs!</h1>\n<h4 align=\"center\">This blog has no welcome page<br/>if you're maintainer of this blog, kindly write either README.md or notebooks/welcome.ipynb file!</h4>\n</body>\n</html>\n")
                        f.close()
        if tipe == "Xbook":
            shutil.rmtree(des)
            ccc.success("deleting " + des)
        return True
    except Exception as err:
        closer.close(err=err, fail="while deleting " + des)
