#!/usr/bin/env python

import os
import time
from Xbooks_converter.repoClonnerAndFetcher import ClonnerAndFetcher
from Xbooks_converter.repoCommiterAndPusher import CommiterAndPusher
from Xbooks_converter import common_cli_conventions as ccc
from Xbooks_converter import jupy2html
from Xbooks_converter import fileRemoverAndRenamer as frandr

IsConverted = False

def getXrc(folder):
    """
    reads and returns the .Xbooksrc file as an object
    """
    with open(os.path.join(folder, ".Xbooksrc"), 'r') as XrcFile:
            XrcData = XrcFile.read()
            XrcFile.close()
    ccc.success("reading Xbooksrc")
    return eval(XrcData)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        candf = ClonnerAndFetcher(sys.argv[1])
        clonned_repo = candf.clone()
        if clonned_repo:
            xrc = getXrc("Xblog")
            if xrc:
                if clonned_repo.author == xrc["GitHub_Username"]:
                    fetched_data = candf.fetch()
                    if fetched_data:
                        ccc.note(str(fetched_data).replace(",", ",\n\t "))
                        sc = []
                        for tbc in fetched_data["to_be_converted"]:
                            sc.append(jupy2html.convert(os.path.join("Xblog", tbc)))
                            if not sc[-1]:
                                break
                        if(all(sc)):
                            sd = []
                            for tbd in fetched_data["to_be_deleted"]:
                                sd.append(frandr.delete(tbd))
                                if not sd[-1]:
                                    break
                            if(all(sd)):
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
                                    if not sr0[-1]:
                                        break
                                for tbrfile in tbrfiles:
                                    sr1.append(frandr.rename(tbrfile))
                                    if not sr1[-1]:
                                        break
                                sr = sr0 and sr1
                                if(all(sr)):
                                    push_url = "https://"+xrc["GitHub_Username"]+":"+sys.argv[2]+"@github.com/"+xrc["GitHub_Username"]+"/"+xrc["gh_repo_name"]+".git"
                                    candp = CommiterAndPusher(push_url, xrc["GitHub_Username"], xrc["Email"])
                                    candp.commit(fetched_data)
                                    # candp.push()
                else:
                    ccc.note("skipping conversion process since latest commit is not authored by the owner " + xrc["GitHub_Username"] + " but is by " + clonned_repo.author)
    else:
        ccc.fail("kindly recheck yor argumentation!")

# python Xbooks.py https://github.com/XinYaanZyoy/test_Xblog 0e5e2e5fc38490096b5febe75a2c842fbfcb930b