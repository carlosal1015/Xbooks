#!/usr/bin/env python

import os
from git import Repo
from git import Actor
import time, datetime
from Xbooks_converter import common_cli_conventions as ccc

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

    def commit(self):
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
        self.commit_message = "Xbooks["+stamp+"]: " + str(msg + " by ") + str(master.commit.author) + ":" + str(master.commit.hexsha[:7])
        self.repo.index.commit(self.commit_message, author=self.author, committer=self.committer)
        ccc.success("commiting changes by \nAuthor:" + str(self.author) + "\nCommitter:" + str(self.committer))
        return self

    def push(self):
        Xorigin = self.repo.create_remote("Xorigin", url=self.url)
        Xorigin.push()
        ccc.success("pushing latest commit " + str(self.repo.head.commit)[:7])
        return self.commit_message

if __name__ == "__main__":
    print("heyy")
