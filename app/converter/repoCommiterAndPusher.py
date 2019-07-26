#!/usr/bin/env python

import os
import sys
from git import Repo
from git import Actor
import time, datetime

from Xlib import ccc
from Xlib import workspaceCleaner as wc

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

class CommiterAndPusher():
    def __init__(self, url, author, email):
        self.repo = Repo("./Xblog")
        self.url = url
        self.author = Actor("Xbooks[bot]", "")
        self.committer = Actor(author, email)

    def commit(self, fetched_data):
        if len(fetched_data["to_be_converted"]) + len(fetched_data["to_be_deleted"]) + len(fetched_data["to_be_renamed"]) != 0:
            try:
                self.repo.git.add(A=True)
                ccc.white("Status" ,str(self.repo.git.status()))
                master = self.repo.head.reference
                stamp = datetime.datetime.fromtimestamp(time.time()) \
                                            .strftime('%H:%M.%S|%y[%m]%d') \
                                            .replace(datetime.datetime \
                                            .fromtimestamp(time.time()) \
                                            .strftime('%H:%M.%S|%y[%m]%d')[-6:-2], \
                                            months[datetime.datetime.fromtimestamp(time.time()) \
                                            .strftime('%H:%M.%S|%y[%m]%d')[-6:-2]])
                msg = master.commit.message
                self.commit_message = "Xbooks["+stamp+"]: " + str(msg.replace("\n", "") + " by ") + str(master.commit.author) + ":" + str(master.commit.hexsha[:7])
                self.repo.index.commit(self.commit_message, author=self.author, committer=self.committer)
                ccc.success("commiting changes by")
                ccc.white("Author:", str({"username": str(self.author), "email": "<>"}))
                ccc.white("Committer:", str({"username": str(self.committer.name), "email": str(self.committer.email)}))
                ccc.white("Commit message", str(self.commit_message))
                return True
            except:
                self.commit_message = ""
                ccc.fail("while commiting Xbooks' changes")
                wc.cleanXblog()
                sys.exit()
        else:
            ccc.alert("there's nothing to commit")
            self.commit_message = ""
            sys.exit()

    def push(self):
        if self.commit_message != "":
            ccc.magenta("Pushing", str(self.repo.head.commit)[:7])
            try:
                Xorigin = self.repo.create_remote("Xorigin", url=self.url)
                Xorigin.push()
                ccc.success("pushing " + str(self.repo.head.commit)[:7])
                return True
            except:
                ccc.fail("while pushing Xbooks' commit")
                wc.cleanXblog()
                sys.exit()

if __name__ == "__main__":
    ccc.greet("hola!")