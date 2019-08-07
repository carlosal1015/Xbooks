#!/usr/bin/env python

import os, sys
import shutil
from bs4 import BeautifulSoup
import time, datetime
import shutil

from Xlib import ccc
from Xlib import XbooksrcReader
from Xlib import workspaceCleaner as wc


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
    

def linkAssets(des, Xrc):
    """
    links css and js to newly converted jupyter notebooks
    """
    with open(des, 'r') as f:
        body = f.read()
        f.close()
    with open(des, 'w') as f:
        body = body.replace("custom.css", "\\" + Xrc["gh_repo_name"] + "/Assets" + "/css" + "/custom.css")
        f.write(body)
        f.close()
    ccc.success("linking assets to " + des)


def addToNavBar(des, tipe, Xrc):
    """
    adds Xpage or Xbook on the navbar
    """
    try:
        title = des.split("/")[-1].replace(".html", "")
        new_nav = "<li id=\"$ID$\"><a style=\"cursor: pointer\" onclick=\"document.getElementById(\'Xdisplay\').contentWindow.location.replace(\'$LINK$\'); updateExplorer(\'$LINK$\')\">$TITLE$</a></li>\n\t\t\t\t\t\t\t<!-- $XBOOKS_NAV$ -->"
        nav = "<!-- $XBOOKS_NAV$ -->"

        with open("Xblog/docs/index.html", 'r') as f:
            index = f.read()
            f.close()

        with open("Xblog/docs/index.html", 'w') as f:
            if tipe == "Xbook":
                index = index.replace(nav, new_nav.replace("$ID$", title).replace('$TITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + title + '/index.html'))
            if tipe == "Xpage":
                index = index.replace(nav, new_nav.replace("$ID$", title).replace('$TITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + title + '.html'))
            f.write(index)
            f.close()
        ccc.success("adding " + title + " to navigation pallete")
    except:
        ccc.fail("adding " + title + " to navigation pallete")
        wc.cleanXblog()
        sys.exit()

def addToParentIndex(des, tipe, Xrc):
    """
    adds Xpage or Xbook on parent's index
    """
    print("toindex ", des)
    try:
        title = des.split("/")[-1].replace(".html", "")
        index = des.replace(os.path.basename(des), "index.html")

        band = "<!-- $BAND$ -->"
        new_band = "<tr id=\"$ID$\" onclick=\"window.location.replace('$LINK$'); updateExplorer_IFrame('$LINK$');\" style=\"background-color: rgb(55, 57, 58); width: 100vw; box-shadow: gray 2px 2px 2px;\"><th scope='row' style=\"border: none; width: 60vw;\">$XTITLE$</th><td style=\"border: none; width: 40vw;\">$TIMESTAMP$</td></tr>" + "\n\t" + band 

        card = "<!-- $CARD$ -->"
        start = "<td id=\"$ID$\"><div onclick=\"window.location.replace('$LINK$'); updateExplorer_IFrame(\'$LINK$\');\" class=\"card bg-light mb-3\" style=\"max-width: 20rem; background-color: rgba(39, 39, 39, 0.819) !important; color: rgb(200, 192, 188) !important; border: none; box-shadow: gray 5px 5px 5px;\"><div class=\"card-header\" style=\"background-color: rgba(37, 37, 37, 0.877) !important; border: none; color: white;\">$XTITLE$</div>"
        img = "<div class=\"card-body\"><img style=\"height: 256px; width: 256px; display: block; filter: saturate(0.7) brightness(0.5);\" src=\"$CARD_IMG_SRC$\"></div>"
        end = "</div></td>"

        new_card_img = start + img + end + "\n\t" + card
        new_card_noimg = start + end + "\n\t" + card

        with open(index, 'r') as f:
            body = f.read()
            f.close()
        with open(index, 'w') as f:
            notebook = "/".join(des.split("/")[2:])
            body = body.replace('$TITLE$', 'TOC of ' + des.replace(des.split("/")[-1], ""))
            if tipe == "Xpage":
                body = BeautifulSoup(body.replace(band, new_band.replace("$ID$", title).replace('$XTITLE$', title).replace('$TIMESTAMP$', datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M.%S|$MONTH$ %d %Y by Xbooks[bot]").replace("$MONTH$", chooseMonth(datetime.datetime.fromtimestamp(time.time()).strftime("%m")))).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + notebook)), 'html.parser').prettify()
            if tipe == "Xbook":
                notebook = notebook + "/index.html"
                if os.path.exists(des.replace("docs/", "") + "/card.png"):
                    shutil.copy2(des.replace("docs/", "") + "/card.png", des + "/card.png")
                    ccc.note("copied " + des.replace("docs/", "") + "/card.png to" + des + "/card.png")
                    body = BeautifulSoup(body.replace(card, new_card_img.replace("$ID$", title).replace('$XTITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + notebook).replace("$CARD_IMG_SRC$", title+"/card.png")), 'html.parser').prettify()
                else:
                    body = BeautifulSoup(body.replace(card, new_card_noimg.replace("$ID$", title).replace('$XTITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + notebook)), 'html.parser').prettify(formatter="html")
            f.write(body)
            f.close()
        ccc.success("adding " + des + " to parent index")
    except:
        ccc.fail("adding " + des + " to parent index")
        wc.cleanXblog()
        sys.exit()


def install(des, tipe):
    """
    called at every creation of Xbook or Xpage
    """
    try:
        Xrc = XbooksrcReader.read("Xblog")
        if tipe == "Xbook":
            src = "Xblog/docs/Assets/html/index.html"
            shutil.copy2(src, des)
            ccc.success("installing index of " + des)
            if des.replace(os.path.basename(des), "") == "Xblog/docs/notebooks/":
                addToNavBar(des, tipe, Xrc)
            else:
                addToParentIndex(des, tipe, Xrc)

        if tipe == "Xpage":
            linkAssets(des, Xrc)
            if des.replace(os.path.basename(des), "") == "Xblog/docs/notebooks/":
                if not des.endswith("welcome.html"):
                    addToNavBar(des, tipe, Xrc)
            else:
                addToParentIndex(des, tipe, Xrc)
        ccc.success("installtion procedures for " + des)
    except:
        ccc.fail("while installation procedures for " + des)
        wc.cleanXblog()
        sys.exit()