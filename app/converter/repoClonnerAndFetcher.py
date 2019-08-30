#!/usr/bin/env python

import os
import sys
from git import Repo
import json

from Xlib import ccc
from Xlib import ignoreReader
from Xlib import XbooksrcReader
from Xlib import closer


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
        closer.close(fail="while parsing file status code")


def fetch_untransformed_commits():
    """
    fetches untransformed commits' hexsha7 from transform key of Xrc
    """
    try:
        ccc.note("fetching untransformed commits")
        xrc = XbooksrcReader.read("Xblog")
        if "transform" in xrc:
            return xrc["transform"]
        else:
            return []
    except Exception as err:
        closer.close(err=err, fail="fetching untransformed commits")


def update_Xrc_transform(hexsha7):
    """
    stores latest fetched data to transfrom key of Xrc
    """
    try:
        ccc.note('logging ' + hexsha7)
        xrc = XbooksrcReader.read("Xblog")
        if not "transform" in xrc:
            xrc.update({"transform":[]})
        xrc["transform"].append(hexsha7)
        with open("Xblog/.Xbooksrc", 'w') as f:
            f.write(json.dumps(xrc, sort_keys=True, indent=4))
            f.close()
        ccc.success("updating transform key in .Xbooksrc")
    except Exception as err:
        closer.close(err=err, fail="updating transform key in .Xbooksrc")


def fetch_from_commit(Obj_hexsha7, hexsha7):
    """
    returns dict of data of analysis of given commit hexsha7
    """
    try:
        ignore_list = ignoreReader.read()
        to_delete = []
        to_rename = []
        to_convert = []
        ccc.white("Fetching", hexsha7)
        for fn, fd in list(Obj_hexsha7.stats.files.items()):
            if fn.startswith("notebooks") and fn not in ignore_list and "checkpoint" not in fn and ".ipynb" in fn:
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
                    closer.close(fail="while decoding status code")
        ccc.success("fetching " + hexsha7)
        return {
            "to_be_converted": to_convert,
            "to_be_deleted": to_delete,
            "to_be_renamed": list(set(to_rename))
            }
    except Exception as err:
        closer.close(err=err, fail="fetching " + hexsha7)


class ClonnerAndFetcher:
    """
    clone, fetch, filter, and return
    """
    def __init__(self, url):
        self.url = url
        self.repo = None
        self.author = None

    def clone(self):
        """
        clones git repository returns true if success; failure otherwise
        """
        try:
            ccc.white("Clonning", self.url)
            self.repo = Repo.clone_from(self.url, "./Xblog", branch="master")
            self.author = self.repo.head.commit.author.name
            ccc.success("clonning " + self.url)
            return self
        except Exception as err:
            closer.close(err=err, fail="clonning repo " + self.url, note="kindly first delete the repo which(if) already exist!\nor check if the remote repo exists!")


    def fetch(self):
        """
        fetches repo
        """
        try:
            to_be_transformed = []
            for commit in fetch_untransformed_commits():
                to_be_transformed.append({"hexsha7":commit, "tree":fetch_from_commit(self.repo.commit(commit), commit)})
            latest = str(self.repo.head.ref.commit.hexsha[:7])
            update_Xrc_transform(latest)
            to_be_transformed.append({"hexsha7":latest, "tree":fetch_from_commit(self.repo.commit(latest), latest)})
            return to_be_transformed
        except Exception as err:
            closer.close(err=err, fail="while fetching commits")
