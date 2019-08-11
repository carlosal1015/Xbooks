#!/usr/bin/env python

import os
import sys
import itertools
from git import Repo

from Xlib import ccc
from Xlib import workspaceCleaner as wc

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
    else:
        ccc.fail("while parsing file status code")

class ClonnerAndFetcher:
    def __init__(self, url):
        self.url = url

    def clone(self):
        """
        clones git repository returns true if success; failure otherwise
        """
        try:
            ccc.white("Clonning", self.url)
            self.repo = Repo.clone_from(self.url, "./Xblog", branch="mater")
            self.author = self.repo.head.commit.author.name
            ccc.success("clonning " + self.url)
            return self
        except Exception as err:
            ccc.fail("clonning repo " + self.url)
            ccc.note("kindly first delete the repo which(if) already exist!\nor check if the remote repo exists!")
            sys.exit(ccc.stderr(err))

    def fetch(self):
        try:
            toDelete = []
            toRename = []
            toConvert = []
            ccc.white("Fetching", str(self.repo.head.commit)[:7])
            for fn, fd in list(self.repo.head.commit.stats.files.items()):
                if fn.startswith("notebooks") and fn not in [] and "checkpoint" not in fn and ".ipynb" in fn:
                    status = fstatus(fd['insertions'], fd['deletions'], fd['lines'])
                    ccc.note("fetched " + fn + " with status " + status)
                    if status != "110" and status != "100" and status != "010":
                        if os.path.exists(os.path.join("Xblog", fn)) and fn.endswith(".ipynb"):
                            if status == "111" or status == "101" or status == "011":
                                toConvert.append(fn)
                        else:
                            if status == "011" and fn.endswith(".ipynb"):
                                toDelete.append(fn)
                        if status == "000":
                            src = os.path.join(fn.split("{")[0], fn.split("{")[1].split(" => ")[0])
                            des = os.path.join(fn.split("{")[0], fn.split("{")[1].split(" => ")[1].split("}")[0])
                            # if src.endswith(".ipynb") and des.endswith(".ipynb"):
                            toRename.append((src, des))
                    else:
                        ccc.fail("while decoding status code")
                        wc.cleanXblog()
                        sys.exit()
            ccc.success("fetching " + str(self.repo.head.commit)[:7])
            return {
                    "to_be_converted": toConvert,
                    "to_be_deleted": toDelete,
                    "to_be_renamed": list(set(toRename))
                    }
        except Exception as err:
            ccc.fail("while fetching latest commit changes")
            wc.cleanXblog()
            sys.exit(ccc.stderr(err))