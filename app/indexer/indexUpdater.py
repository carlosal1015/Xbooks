#!/usr/bin/env python

import os
import sys
from bs4 import BeautifulSoup
import time, datetime

from Xlib import ccc
from Xlib import XbooksrcReader
from Xlib import closer


def chooseMonth(num):
    """
    returns texted month
    """
    if num == "01":
        return "JAN"
    if num == "02":
        return "FEB"
    if num == "03":
        return "MAR"
    if num == "04":
        return "APR"
    if num == "05":
        return "MAY"
    if num == "06":
        return "JUN"
    if num == "07":
        return "JUL"
    if num == "08":
        return "AUG"
    if num == "09":
        return "SEP"
    if num == "10":
        return "OCT"
    if num == "11":
        return "NOV"
    if num == "12":
        return "DEC"
    return "UNKNOWN"


def editNavBar(src, des, tipe, Xrc):
    """
    edits Xbook or Xpage on navbar
    """
    try:
        print("this is nav bar")
        old_title = src.split("/")[-1].replace(".html", "")
        new_title = des.split("/")[-1].replace(".html", "")
        index = "Xblog/docs/index.html"
        with open(index, 'r') as f:
            soup = BeautifulSoup(f, "html.parser")
            f.close()
        tag = soup.select("#"+old_title)[0]
        old_src = tag.a["onclick"].split("; ")[1].split('(')[1].split(')')[0]
        if tipe == 'Xbook':
            new_src = '\'\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + new_title + '/index.html\''
        if tipe == 'Xpage':
            new_src = '\'\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + new_title + '.html\''
        tag.a.string = tag.a.string.replace(old_title, new_title)
        tag.a["onclick"] = tag.a["onclick"].replace(old_src, new_src)
        tag.a["id"] = new_title
        with open(index, 'w') as f:
            f.write(soup.prettify(formatter="html"))
            f.close()
        ccc.success("updating " + des + " from navigation pallete")
    except Exception as err:
        closer.close(err=err, fail="while updating " + des + " from navigation pallete")


def editParentIndex(src, des, tipe, Xrc):
    """
    edits Xbook or Xpage on parent's index
    """
    try:
        print("this is parent index")
        old_title = src.split("/")[-1].replace(".html", "")
        new_title = des.split("/")[-1].replace(".html", "")
        index = des.replace(os.path.basename(des), "index.html")
        with open(index, 'r') as f:
            soup = BeautifulSoup(f, "html.parser")
            f.close()
        tag = soup.select("#"+old_title)[0]
        print(tag)
        print(tag["onclick"])
        print(tag["onclick"].split(";"))
        old_tstamp = tag.td.string.lstrip().rstrip()
        new_tstamp = datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M.%S|$MONTH$ %d %Y by Xbooks[bot]").replace("$MONTH$", chooseMonth(datetime.datetime.fromtimestamp(time.time()).strftime("%m")))
        old_src = tag["onclick"].split(";")[0].split('(')[1].split(')')[0]
        if tipe == 'Xbook':
            new_src = '\'\\\\' + Xrc["gh_repo_name"] + '/' + "/".join(des.split("/")[2:]) + "/index.html\'"
        if tipe == 'Xpage':
            new_src = '\'\\\\' + Xrc["gh_repo_name"] + '/' + "/".join(des.split("/")[2:]) + "\'"
        tag.td.string = tag.td.string.replace(old_tstamp, new_tstamp)
        tag.th.string = tag.th.string.replace(old_title, new_title)
        tag["onclick"] = tag["onclick"].replace(old_src, new_src)
        tag["id"] = new_title
        with open(index, 'w') as f:
            f.write(soup.prettify(formatter="html"))
            f.close()
        ccc.success("updating " + des + " from parent index")
    except Exception as err:
        closer.close(err=err, fail="while updating " + des + " from parent index")


def update(src, des, tipe):
    """
    called at every rename of Xbook or Xpage
    """
    try:
        Xrc = XbooksrcReader.read("Xblog")
        print(src, des, tipe)
        src = "Xblog/docs/" + src
        des = "Xblog/docs/" + des
        print(src, des, tipe)
        if "Xblog/docs/notebooks/" == des.replace(os.path.basename(des), ""):
            editNavBar(src, des, tipe, Xrc)
        else:
            editParentIndex(src, des, tipe, Xrc)
        ccc.success("updatation procedures for " + des)
    except Exception as err:
        closer.close(err=err, fail="while updatation procedures for " + des)
