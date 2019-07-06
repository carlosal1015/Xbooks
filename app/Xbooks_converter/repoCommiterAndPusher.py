#!/usr/bin/env python

import os
from git import Repo
import time, datetime

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
    def __init__(self, url):
        self.url = url

    def commit(self):
        self.repo = Repo("./Xbooks")
        self.repo.git.add(update=True)
        master = self.repo.head.reference
        stamp = datetime.datetime.fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d') \
                                    .replace(datetime.datetime \
                                    .fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2], \
                                    months[datetime.datetime.fromtimestamp(time.time()) \
                                    .strftime('%H:%M.%S|%y[%m]%d')[-6:-2]])
        msg = master.commit.message.split(":")[2:-2]
        self.commit_message = "Xbooks["+stamp+"]: " + str(msg) + "\ncommit: " + str(master.commit.hexsha) + " by " + str(master.commit.author)
        self.repo.index.commit(self.commit_message)
        return self

    def push(self):
        origin = self.repo.remote(name='origin')
        origin.push()
        return self.commit_message

if __name__ == "__main__":
    print("heyy")