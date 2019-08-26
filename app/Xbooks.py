#!/usr/bin/env python

import os
import time
import shutil

from Xlib import ccc

ccc.greet("hola! lots of hopes and wishes for your project! from the writter of Xbooks; XinYaanZyoy! \
       \nhttps://GitHub.com/XinYaanZyoy")
ccc.alert("Xbooks is still under development process!!")

from Xlib import workspaceCleaner as wc
from Xlib import XbooksrcReader

import converter.fileRemoverAndRenamer as frandr
import converter.jupy2html as jupy2html
import converter.jupy2pdf as jupy2pdf
from converter.repoClonnerAndFetcher import ClonnerAndFetcher
from converter.repoCommiterAndPusher import CommiterAndPusher

from indexer import indexUpdater as IUp
from indexer import indexUninstaller as IUn

# the problem here is, there's not need for tracking
# tipe == "Xbook" beacuse git doesn't report it!(perhaps)

# this script can be run only on cli
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        candf = ClonnerAndFetcher(sys.argv[1])
        clonned_repo = candf.clone()
        if clonned_repo:
            xrc = XbooksrcReader.read("Xblog")
            if xrc:
                if clonned_repo.author == xrc["GitHub_Username"]:
                    fetched_data = candf.fetch()
                    if fetched_data:
                        ccc.note(str(fetched_data).replace(",", ",\n\t "))
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
                                        wc.cleanXblog()
                                    # print("woodoo!")
                else:
                    ccc.note("skipping transformation process since latest commit is not authored by the owner " + xrc["GitHub_Username"] + " but is by " + clonned_repo.author)
                    wc.cleanXblog()
                    sys.exit()
    else:
        ccc.fail("kindly recheck yor argumentation!")
        sys.exit()

# python Xbooks.py https://github.com/XinYaanZyoy/test_Xblog 0e5e2e5fc38490096b5febe75a2c842fbfcb930b