#!/usr/bin/env python

import os
import sys
import json

from Xlib import ccc
from Xlib import XbooksrcReader
from Xlib import closer

import converter.fileRemoverAndRenamer as frandr
import converter.jupy2html as jupy2html
import converter.jupy2pdf as jupy2pdf
from converter.repoCommiterAndPusher import CommiterAndPusher

from indexer import indexUninstaller as IUn


# the problem here is, there's not need for tracking
# tipe == "Xbook" beacuse git doesn't report it!(perhaps)


def update_Xrc_transform(hexsha7):
    """
    delets hexsha7 from transform key of .Xbooksrc
    """
    try:
        ccc.note('untracking ' + hexsha7)
        xrc = XbooksrcReader.read("Xblog")
        xrc["transform"].pop(hexsha7)
        with open("Xblog/.Xbooksrc", 'w') as f:
            f.write(json.dumps(xrc, sort_keys=True, indent=4))
            f.close()
        ccc.success("updating transform key in .Xbooksrc")
    except Exception as err:
        closer.close(err=err, fail="updating transform key in .Xbooksrc")

def transform(hexsha7, fetched_data):
    """
    """
    try:
        xrc = XbooksrcReader.read("Xblog")
        ccc.note("transforminng "+hexsha7+" having tree\n"+str(fetched_data).replace(",", ",\n\t "))
        sr0 = []
        sr1 = []
        tbrdirs = []
        tbrfiles = []
        for tbr in fetched_data["to_be_renamed"]:
            if '.ipynb' not in os.path.basename(tbr[0]) and '.ipynb' not in os.path.basename(tbr[1]):
                tbrdirs.append(tbr)
            else:
                if '.ipynb' in os.path.basename(tbr[0]) and '.ipynb' in os.path.basename(tbr[1]):
                    tbrfiles.append(tbr)
                else:
                    ccc.fail("something is wrong in file naming of" + str(tbr))
        for tbrdir in tbrdirs:
            sr0.append(frandr.rename(tbrdir, 'Xbook'))
        for tbrfile in tbrfiles:
            sr1.append(frandr.rename(tbrfile, 'Xpage'))
        if all(sr0) and all(sr1):
            sc = []
            for tbc in fetched_data["to_be_converted"]:
                sc.append(jupy2html.convert("Xblog/" + tbc))
                sc.append(jupy2pdf.convert("Xblog/" + tbc))
        if(all(sc)):
            sd0 = []
            sd1 = []
            tbddirs = []
            tbdfiles = []
            for tbd in fetched_data["to_be_deleted"]:
                if '.ipynb' not in os.path.basename(tbd):
                    tbddirs.append(tbd)
                else:
                    if '.ipynb' in os.path.basename(tbd):
                        tbdfiles.append(tbd)
                    else:
                        ccc.fail("something is wrong in file naming of" + str(tbd))
            # perhaps git internally doesn't report deletation of whole directory
            # but instead reports all files within that directory as been deleted!
            for tbdfile in tbdfiles:
                sd0.append(frandr.delete(tbdfile, "Xpage"))
                des = "Xblog/docs/" + tbdfile.replace(".ipynb", ".html")
                index = des.replace(os.path.basename(des), "index.html")
                root = index.replace("index.html", "")
                ccc.note("checking if " + root + " is empty...")
                arr = os.listdir(root)
                print(arr)
                if arr == ["index.html"]:
                    root = "/".join(root.split("/")[:-1])
                    IUn.uninstall(root)
                    os.remove(root+"/index.html")
                    os.rmdir(root)
                    ccc.success("deleting " + root)
                    root_pdf = root.replace("notebooks", "pdfs")
                    os.rmdir(root_pdf)
                for tbddir in tbddirs:
                    sd1.append(frandr.delete(tbddir, "Xbook"))
            if(all(sd0) and all(sd1)):
                push_url = "https://"+xrc["GitHub_Username"]+":"+sys.argv[2]+"@github.com/"+xrc["gh_repo_namespace"]+"/"+xrc["gh_repo_name"]+".git"
                candp = CommiterAndPusher(push_url, xrc["GitHub_Username"], xrc["Email"])
                if candp.commit(fetched_data):
                    if candp.push():
                        ccc.success("transforming "+hexsha7)
                        update_Xrc_transform(hexsha7)
                        # print("woodoo!")
    except Exception as err:
        closer.close(err=err, fail="transforming "+hexsha7)
