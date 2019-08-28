#!/usr/bin/env python

from Xlib import ccc

ccc.greet("hola! lots of hopes and wishes for your project! from the writter of Xbooks; XinYaanZyoy! \
       \nhttps://GitHub.com/XinYaanZyoy")
ccc.alert("Xbooks is still under development process!!")

from Xlib import workspaceCleaner as wc
from Xlib import XbooksrcReader

from converter.repoClonnerAndFetcher import ClonnerAndFetcher

import transformer

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
                    commits = candf.fetch()
                    if commits:
                        for commit in commits:
                            transformer.transform(commit["hexsha7"], commit["tree"])
                        ccc.cyan("THANKS", "for using Xbooks!, visit me @ XinYaanZyoy.github.io")
                else:
                    ccc.note("skipping transformation process since latest commit is not authored by the owner " + xrc["GitHub_Username"] + " but is by " + clonned_repo.author)
                    wc.cleanXblog()
                    sys.exit()
    else:
        ccc.fail("kindly recheck your argumentation!")
        ccc.note("check whether env vars set properly! or check your CI script if it's not currepted")
        sys.exit()
