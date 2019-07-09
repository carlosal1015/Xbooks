#!/usr/bin/env python

import os
import time
from Xbooks_converter.repoClonnerAndFetcher import ClonnerAndFetcher
from Xbooks_converter.repoCommiterAndPusher import CommiterAndPusher
from Xbooks_converter import common_cli_conventions as ccc

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
        xrc = getXrc("Xblog")
        if clonned_repo.author == xrc["GitHub_Username"]:
            ccc.note(str(candf.fetch()))

            with open("./Xblog/byXbooks"+str(time.time()), 'a') as f:
                f.write("\n"+ str(time.time()) +"holaaa!!")
            ccc.success("writing temp file")

            push_url = "https://"+xrc["GitHub_Username"]+":"+sys.argv[2]+"@github.com/"+xrc["GitHub_Username"]+"/"+xrc["gh_repo_name"]+".git"
            candp = CommiterAndPusher(push_url, xrc["GitHub_Username"], xrc["Email"])
            ccc.white("Commit", str(candp.commit().push()))
        else:
            ccc.fail("the latest commit is not authored by the owner " + xrc["GitHub_Username"] + " but is by " + clonned_repo.author)
    else:
        ccc.fail("kindly recheck yor argumentation!")

# python Xbooks.py https://github.com/XinYaanZyoy/test_Xblog 51df0ace734c94c3d1026080a7439610cb5e4707