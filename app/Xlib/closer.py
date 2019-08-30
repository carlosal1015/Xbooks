import os
import sys
from git import Repo, Actor
import time, datetime

from . import ccc

closeCode = 0

months = {
    "[01]": "A",
    "[02]": "B",
    "[03]": "C",
    "[04]": "D",
    "[05]": "E",
    "[06]": "F",
    "[07]": "G",
    "[08]": "H",
    "[09]": "I",
    "[10]": "J",
    "[11]": "K",
    "[12]": "L"
}


def update_Xbooksrc_transform():
    """
    commits and pushes updated Xbooksrc at every failure but before cleaning and exiting
    """
    global closeCode
    try:
        print("\n\nproceeding to closing script...")
        repo = Repo("./Xblog")
        author = Actor("Xbooks[bot]", "")
        committer = Actor("Xbooks[bot]", "")
        repo.git.add([".Xbooksrc"])
        ccc.white("Status" ,str(repo.git.status()))
        if not "nothing to commit" in str(repo.git.status()):
            master = repo.head.reference
            msg = master.commit.message
            stamp = datetime.datetime.fromtimestamp(time.time()) \
                                                    .strftime('%H:%M.%S|%y[%m]%d') \
                                                    .replace(datetime.datetime \
                                                    .fromtimestamp(time.time()) \
                                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2], \
                                                    months[datetime.datetime.fromtimestamp(time.time()) \
                                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2]])
            commit_message = "chores: Xbooks["+stamp+"] => " + str(msg.replace("\n", "") + " by ") + str(master.commit.author) + ":" + str(master.commit.hexsha[:7]) + "[skip ci]"
            repo.index.commit(commit_message, author=author, committer=committer)
            ccc.success("commiting changes by")
            ccc.white("Author:", str({"username": str(author), "email": ""}))
            ccc.white("Committer:", str({"username": str(committer.name), "email": str(committer.email)}))
            ccc.white("Commit message", str(commit_message))
            ccc.magenta("Pushing chores as ", str(repo.head.commit)[:7])
            repo.remotes.origin.push()
            ccc.success("pushing chores as" + str(repo.head.commit)[:7])
        else:
            ccc.note("no chores to be commited and pushed")
    except Exception as err:
        ccc.fail(err+"\n the stable flow has been broken kindly handle untransformd commits manually!")
        closeCode = 1

def close(err="", fail="", note="", success="", cyan=[], alert=""):
    """
    print failure,
    clean workspace
    exit with stderr
    """
    global closeCode

    if err != "":
        ccc.stderr(err)
        closeCode = 1
    if cyan != []:
        ccc.cyan(cyan[0], cyan[1])
    if note != "":
        ccc.note(note)
    if fail != "":
        ccc.fail(fail)
        closeCode = 1
    if alert != "":
        ccc.alert(alert)
        closeCode = 1
    if success != "":
        ccc.success(success)
    update_Xbooksrc_transform()
    if "linux" in sys.platform:
        try:
            os.system("rm -r -f ./Xblog/")
            ccc.success("cleaning temp workspace")
        except Exception as err:
            ccc.fail=("cleaning temp workspace")
            closeCode = 1
    else:
        ccc.note("aborted cleaning temp workspace")
        closeCode = 1

    sys.exit(closeCode)