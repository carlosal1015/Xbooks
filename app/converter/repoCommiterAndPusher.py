#!/usr/bin/env python

import os
import sys
from git import Repo
from git import Actor
import time, datetime
import json

from Xlib import ccc
from Xlib import closer
from Xlib import XbooksrcReader

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


def update_Xrc_transform(hexsha7):
    """
    delets hexsha7 from transform key of .Xbooksrc
    """
    try:
        ccc.note('untracking ' + hexsha7)
        xrc = XbooksrcReader.read("Xblog")
        xrc["transform"].pop(hexsha7)
        with open("Xblog/.Xbooksrc", 'w') as f:
            f.write(json.dumps(xrc, sort_keys=True, indent=4))
            f.close()
        ccc.success("updating transform key in .Xbooksrc")
    except Exception as err:
        closer.close(err=err, fail="updating transform key in .Xbooksrc")



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
                self.commit_message = "docs: Xbooks["+stamp+"] => " + str(msg.replace("\n", "") + " by ") + str(master.commit.author) + ":" + str(master.commit.hexsha[:7])
                self.repo.index.commit(self.commit_message, author=self.author, committer=self.committer)
                ccc.success("commiting changes by")
                ccc.white("Author:", str({"username": str(self.author), "email": ""}))
                ccc.white("Committer:", str({"username": str(self.committer.name), "email": str(self.committer.email)}))
                ccc.white("Commit message", str(self.commit_message))
                return True
            except Exception as err:
                self.commit_message = ""
                closer.close(err=err, fail="while commiting Xbooks' changes")
        else:
            self.commit_message = ""
            closer.close(alert="there's nothing to commit", shouldPush=False)
            update_Xrc_transform(str(master.commit.hexsha[:7]))

    def push(self):
        if self.commit_message != "":
            ccc.magenta("Pushing", str(self.repo.head.commit)[:7])
            try:
                Xorigin = self.repo.create_remote("Xorigin", url=self.url)
                Xorigin.push()
                ccc.success("pushing " + str(self.repo.head.commit)[:7])
                return True
            except Exception as err:
                closer.close(err, fail="while pushing Xbooks' commit")
