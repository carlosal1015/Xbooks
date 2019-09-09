#!/usr/bin/env python

import os
from xbooks import ccc, version
ccc.greet("hola! lots of hopes and wishes for your project! from the writter of Xbooks; XinYaanZyoy! \
       \nhttps://GitHub.com/XinYaanZyoy")
ccc.alert("Xbooks "+version+" is still under development process!!")

def transform(hexsha7, fetched_data):
    """
    """
    from xbooks.Xinit import Xrc, Xignore
    from xbooks import i, gh, cnv, e

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
        sr0.append(i.rename(tbrdir, 'Xbook'))
    for tbrfile in tbrfiles:
        sr1.append(i.rename(tbrfile, 'Xpage'))
    if all(sr0) and all(sr1):
        sc = []
        for tbc in fetched_data["to_be_converted"]:
            if tbc == "README.md":
                cnv.md2html()
                continue
            sc.append(cnv.jupy2html("Xblog/" + tbc))
            sc.append(cnv.jupy2pdf("Xblog/" + tbc))
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
            sd0.append(i.delete(tbdfile, "Xpage"))
            des = "Xblog/docs/" + tbdfile.replace(".ipynb", ".html")
            index = des.replace(os.path.basename(des), "index.html")
            root = index.replace("index.html", "")
            ccc.note("checking if " + root + " is empty...")
            arr = os.listdir(root)
            if arr == ["index.html"]:
                root = "/".join(root.split("/")[:-1])
                i.uninstall(root)
                os.remove(root+"/index.html")
                os.rmdir(root)
                ccc.success("deleting " + root)
                root_pdf = root.replace("notebooks", "pdfs")
                os.rmdir(root_pdf)
            for tbddir in tbddirs:
                sd1.append(i.delete(tbddir, "Xbook"))
        if(all(sd0) and all(sd1)):
            push_url = "https://"+Xrc["GitHub_Username"]+":"+sys.argv[2]+"@github.com/"+Xrc["gh_repo_namespace"]+"/"+Xrc["gh_repo_name"]+".git"
            # print("to be commited and pushed!")
            if gh.commit(fetched_data):
                ccc.success("trans")


# this script can be run only on cli

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        from xbooks import Xinit
        Xinit.init(sys.argv[1])
        from xbooks.Xinit import Xrc, author
        if author == Xrc["GitHub_Username"]:
            from xbooks.gh import fetch, commit, push
            tbt = fetch()
            for commit in tbt:
                transform(commit["hexsha7"], commit["tree"])
        else:
            ccc.note("skipping transformation process since latest commit is not authored by the owner " + Xrc["GitHub_Username"] + " but is by " + author)
    else:
        ccc.fail("kindly recheck your argumentation!")
        ccc.note("check whether env vars set properly! or check your CI script if it's not currepted")
        sys.exit()
