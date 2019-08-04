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
from converter.repoClonnerAndFetcher import ClonnerAndFetcher
from converter.repoCommiterAndPusher import CommiterAndPusher

from indexer import indexUpdater as IU

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
                            if '.' not in os.path.basename(tbr[0]) and '.' not in os.path.basename(tbr[1]):
                                tbrdirs.append(tbr)
                            else:
                                if '.' in os.path.basename(tbr[0]) and '.' in os.path.basename(tbr[1]):
                                    tbrfiles.append(tbr)
                                else:
                                    ccc.fail("something is wrong in file naming of" + str(tbr))
                        for tbrdir in tbrdirs:
                            sr0.append(frandr.rename(tbrdir))

                        for tbrfile in tbrfiles:
                            sr1.append(frandr.rename(tbrfile))

                        if all(sr0) and all(sr1):
                            sc = []
                            for tbc in fetched_data["to_be_converted"]:
                                sc.append(jupy2html.convert(os.path.join("Xblog", tbc)))

                        if(all(sc)):
                            sd = []
                            for tbd in fetched_data["to_be_deleted"]:
                                sd.append(frandr.delete(tbd))

                            if(all(sd)):
                                push_url = "https://"+xrc["GitHub_Username"]+":"+sys.argv[2]+"@github.com/"+xrc["GitHub_Username"]+"/"+xrc["gh_repo_name"]+".git"
                                candp = CommiterAndPusher(push_url, xrc["GitHub_Username"], xrc["Email"])
                                if candp.commit(fetched_data):
                                    if candp.push():
                                        wc.cleanXblog()
                else:
                    ccc.note("skipping conversion process since latest commit is not authored by the owner " + xrc["GitHub_Username"] + " but is by " + clonned_repo.author)
                    wc.cleanXblog()
                    sys.exit()
    else:
        ccc.fail("kindly recheck yor argumentation!")
        sys.exit()

# python Xbooks.py https://github.com/XinYaanZyoy/test_Xblog 0e5e2e5fc38490096b5febe75a2c842fbfcb930b