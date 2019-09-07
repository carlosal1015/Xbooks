from xbooks import ccc

Xrc = None
Xignore = None
repo = None
author = None

def clone(url):
    """
    clones git repository returns true if success; failure otherwise
    """
    try:
        global repo, author
        ccc.white("Clonning", url)
        from git import Repo
        repo = Repo.clone_from(url, "./Xblog", branch="master")
        author = repo.head.commit.author.name
        ccc.success("clonning " + url)
        return (repo, author)
    except Exception as err:
        ccc.stderr(err)

def init(url):
    """
    """
    try:
        global Xignore, Xrc, repo, author
        import os
        from . import gh
        repo, author = clone(url)

        with open("Xblog/.Xbooksrc", 'r') as f:
            Xrc = eval(f.read())
            f.close()
            ccc.success("reading Xbooksrc")

        if os.path.exists("Xblog/.Xbooksignore"):
            with open(os.path.join("Xblog/.Xbooksignore"), 'r') as f:
                Xignore = f.read()
                f.close()
                ccc.success("reading Xbooksignore")
                Xignore = Xignore.split("\n")
        else:
            if "ignore" in Xrc:
                Xignore = Xrc["ignore"]
                ccc.success("fetching ignore list")
            else:
                Xignore = []
                ccc.note("ignore list is either empty or undefined")
    except Exception as err:
        ccc.stderr(err)