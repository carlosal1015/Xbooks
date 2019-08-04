#!/usr/bin/env python

import os
import shutil
from bs4 import BeautifulSoup
import time

from Xlib import ccc
from Xlib import XbooksrcReader

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
    title = des.split(os.path.sep)[-1].replace(".html", "")
    new_nav = "<li><a style=\"cursor: pointer\" onclick=\"document.getElementById(\'Xdisplay\').contentWindow.location.replace(\'$LINK$\'); updateExplorer(\'$LINK$\')\">$TITLE$</a></li>\n\t\t\t\t\t\t\t<!-- $XBOOKS_NAV$ -->"
    nav = "<!-- $XBOOKS_NAV$ -->"

    with open(os.path.join("Xblog", "docs", "index.html"), 'r') as f:
        index = f.read()
        f.close()

    with open(os.path.join("Xblog", "docs", "index.html"), 'w') as f:
        if tipe == "Xbook":
            index = index.replace(nav, new_nav.replace('$TITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + title + '/index.html'))
        if tipe == "Xpage":
            index = index.replace(nav, new_nav.replace('$TITLE$', title).replace('$LINK$', '\\\\' + Xrc["gh_repo_name"] + '/' + 'notebooks/' + title + '.html'))
        f.write(index)
        f.close()
    ccc.success("adding " + title + " to navigation pallete")


def addToParentIndex(des, tipe, Xrc):
    """
    adds Xpage or Xbook on parent's index
    """
    title = des.split(os.path.sep)[-1].replace(".html", "")
    index = des.replace(os.path.basename(des), "index.html")

    band = "<!-- $BAND$ -->"
    new_band = "<tr onclick=\"window.location.replace('$LINK$');\" style=\"background-color: rgb(55, 57, 58); width: 100vw; box-shadow: gray 4px 4px 4px;\"><th scope='row' style=\"border: none; width: 60vw;\">$XTITLE$</th><td style=\"border: none; width: 40vw;\">$TIMESTAMP$</td></tr>"

    card = "<!-- $CARD$ -->"
    start = "<td><div class=\"card bg-light mb-3\" style=\"max-width: 20rem; background-color: rgba(39, 39, 39, 0.219) !important; color: rgb(200, 192, 188) !important; border: none; box-shadow: gray 7px 7px 7px;\"><div class=\"card-header\" style=\"background-color: rgba(37, 37, 37, 0.877) !important; border: none;\">$XTITLE$</div>"
    img = "<div class=\"card-body\"><img style=\"height: 256px; width: 256px; display: block; filter: saturate(0.7) brightness(0.5);\" src=\"$CARD_IMG_SRC$\"></div>"
    end = "</div></td>"

    new_card_img = start + img + end
    new_card_noimg = start + end

    with open(index, 'r') as f:
        body = f.read()
        f.close()
    with open(index, 'w') as f:
        body = body.replace('$TITLE$', 'TOC of ' + des.replace(des.split(os.path.sep)[-1], ""))
        if tipe == "Xpage":
            body = BeautifulSoup(body.replace(band, new_band.replace('$XTITLE$', title).replace('$TIMESTAMP$', datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M.%S|$MONTH$ %d %Y by Xbooks[bot]").replace("$MONTH$", chooseMonth(datetime.datetime.fromtimestamp(time.time()).strftime("%m")))).replace('$LINK$', title + '.html')), 'html.parser').prettify()
        if tipe == "Xbook":
            if os.path.exists(os.path.join("Xblog", des, "card.png")):
                body = BeautifulSoup(body.replace(card, new_card_img.replace('$XTITLE$', title).replace('$LINK$', title + '/index.html').replace("$CARD_IMG_SRC$", "card.png")), 'html.parser').prettify()
                pass
            body = BeautifulSoup(body.replace(card, new_card_noimg.replace('$XTITLE$', title).replace('$LINK$', title + '/index.html')), 'html.parser').prettify()
        f.write(body)
        f.close()
    ccc.success("adding " + des + " to parent index")


def install(des, tipe):
    """
    called at every creation of Xbook or Xpage
    """
    Xrc = XbooksrcReader.read("Xblog")
    print(des)
    if tipe == "Xbook":
        src = os.path.join("Xblog", "docs", "Assets", "html", "index.html")
        shutil.copy2(src, des)
        ccc.success("installing index of " + des)
        if des.replace(os.path.basename(des), "") == os.path.join("Xblog", "docs", "notebooks") + "\\":
            addToNavBar(des, tipe, Xrc)
        else:
            addToParentIndex(des, tipe, Xrc)

    if tipe == "Xpage":
        linkAssets(des, Xrc)
        if des.replace(os.path.basename(des), "") == os.path.join("Xblog", "docs", "notebooks") + "\\":
            if not des.endswith("welcome.html"):
                addToNavBar(des, tipe, Xrc)
        else:
            addToParentIndex(des, tipe, Xrc)
    ccc.success("installtion procedures for " + des)