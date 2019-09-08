#!/usr/bin/env python

import os
import sys
from git import Actor
import time, datetime
import json

from xbooks import ccc, cnv, e

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


def fstatus(plus, minus, lines):
    """
    returns git file change status in three digit string
    """
    status = []
    if plus == 0:
        status.append('0')
    else:
        status.append('1')
    if minus == 0:
        status.append('0')
    else:
        status.append('1')
    if lines == 0:
        status.append('0')
    else:
        status.append('1')
    if len(status) == 3:
        return str().join(status)


def fetch_from_commit(Obj_hexsha7, str_hexsha7):
    """
    returns dict of data of analysis of given commit hexsha7
    """
    from xbooks.Xinit import Xignore, Xrc

    # try:
    to_delete = []
    to_rename = []
    to_convert = []
    ccc.white("Fetching", str_hexsha7)
    commited_tree = list(Obj_hexsha7.stats.files.items())
    l_of_fn = []
    for fn, fd in commited_tree:
        l_of_fn.append(fn)
    welcome_ipynb = "notebooks/welcome.ipynb" in l_of_fn or os.path.isfile("Xblog/notebooks/welcome.ipynb")
    if "README.md" in l_of_fn and not welcome_ipynb:
        to_convert.append("README.md")
    for fn, fd in commited_tree:
        if fn.startswith("notebooks") and fn not in Xignore and "checkpoint" not in fn and ".ipynb" in fn:
            status = fstatus(fd['insertions'], fd['deletions'], fd['lines'])
            ccc.note("fetched " + fn + " with status " + status)
            if status != "110" and status != "100" and status != "010":
                if os.path.exists(os.path.join("Xblog", fn)) and fn.endswith(".ipynb"):
                    if status == "111" or status == "101" or status == "011":
                        to_convert.append(fn)
                else:
                    if status == "011" and fn.endswith(".ipynb"):
                        to_delete.append(fn)
                if status == "000":
                    src = os.path.join(fn.split("{")[0], fn.split("{")[1].split(" => ")[0])
                    des = os.path.join(fn.split("{")[0], fn.split("{")[1].split(" => ")[1].split("}")[0])
                    # if src.endswith(".ipynb") and des.endswith(".ipynb"):
                    to_rename.append((src, des))
            else:
                e.close(fail="while decoding status code")
    ccc.success("fetching " + str_hexsha7)
    return {
        "to_be_converted": to_convert,
        "to_be_deleted": to_delete,
        "to_be_renamed": list(set(to_rename))
        }


def fetch():
    """
    fetches repo
    """
    from xbooks.Xinit import repo

    to_be_transformed = []
    latest = str(repo.head.ref.commit.hexsha[:7])
    to_be_transformed.append({"hexsha7":latest, "tree":fetch_from_commit(repo.commit(latest), latest)})
    return to_be_transformed

def commit(fetched_data):
    from xbooks.Xinit import repo
    if len(fetched_data["to_be_converted"]) + len(fetched_data["to_be_deleted"]) + len(fetched_data["to_be_renamed"]) != 0:
        repo.git.add(A=True)
        ccc.white("Status" ,str(repo.git.status()))
        master = repo.head.reference
        stamp = datetime.datetime.fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d') \
                                    .replace(datetime.datetime \
                                    .fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2], \
                                    months[datetime.datetime.fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2]])
        msg = master.commit.message
        author = Actor("Xbooks[bot]", "")
        committer = author
        commit_message = "docs: Xbooks["+stamp+"] => " + str(msg.replace("\n", "") + " by ") + str(master.commit.author) + ":" + str(master.commit.hexsha[:7])
        repo.index.commit(commit_message, author=author, committer=committer)
        ccc.success("commiting changes by")
        ccc.white("Author:", str({"username": str(author), "email": ""}))
        ccc.white("Committer:", str({"username": str(committer.name), "email": str(committer.email)}))
        ccc.white("Commit message", str(commit_message))
        push()
    else:
        ccc.alert("there's nothing to commit for " + str(repo.head.ref.commit.hexsha[:7]))

def push():
    from xbooks.Xinit import repo, Xrc
    ccc.magenta("Pushing", str(repo.head.commit)[:7])
    Xorigin = repo.create_remote("Xorigin", url="https://{}:{}@github.com/{}/{}.git".format(Xrc["GitHub_Username"], sys.argv[2], Xrc["gh_repo_namespace"], Xrc["gh_repo_name"]))
    Xorigin.push()
    ccc.success("pushing " + str(repo.head.commit)[:7])
    return True
