#!/usr/bin/env python

import os
from git import Repo

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
        print("something went wrong!")

class ClonnerAndFetcher:
    def __init__(self, url):
        self.url = url

    def clone(self):
        """
        clones git repository returns true if success; failure otherwise
        """
        self.repo = Repo.clone_from(self.url, "./Xbooks/", branch="master")
        print("successful clonning!")
        return self

    def fetch(self):
        """
        fetches changes and returns dict with keys convert, delete, and rename
        """
        toDelete = []
        toRename = []
        toConvert = []
        for fn, fd in list(self.repo.iter_commits())[0].stats.files.items():
            status = fstatus(fd['insertions'], fd['deletions'], fd['lines'])
            if fn.startswith("notebooks") and fn not in []:
                if status != "110" and status != "100" and status != "010":
                    if os.path.exists(os.path.join("Xbooks", fn)):
                        if status == "111" or status == "101" or status == "011":
                            toConvert.append(fn)
                    else:
                        if status == "011":
                            toDelete.append(fn)
                    if status == "000":
                            toRename.append(fn)
        return {
                "toConvert": toConvert,
                "toDelete": toDelete,
                "toRename": toRename
                }

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print("clonning...")
        temp_object = ClonnerAndFetcher(sys.argv[1])
        repo = temp_object.clone()
        print("clonned!")
        print("fetchng changes")
        print(repo.fetch())
    else:
        print("kindly specify the url to be clonned and fetched!")