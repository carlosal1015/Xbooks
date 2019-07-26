#!/usr/bin/env python

import os
import shutil
from bs4 import BeautifulSoup

from Xlib import ccc


def linkAssets(des):
    """
    links css and js to newly converted jupyter notebooks
    """
    with open(des, 'r') as f:
        body = f.read()
        f.close()
    with open(des, 'w') as f:
        body = body.replace("custom.css", os.path.join("/", "Assets", "css", "custom.css"))
        f.write(body)
        f.close()
    ccc.success("linking assets to " + des)


def addToNavBar(des, tipe):
    """
    adds Xpage or Xbook on the navbar
    """
    title = des.split(os.path.sep)[-1].replace(".html", "")
    new_nav = "<li><a onclick=\"document.getElementById(\'Xdisplay\').contentWindow.location.replace(\'${link}$\')\">${Xbook/Xpage}$</a></li>\n\t\t\t\t\t\t\t<!-- ${Xbooks_nav}$ -->"
    nav = "<!-- ${Xbooks_nav}$ -->"

    with open(os.path.join("Xblog", "docs", "index.html"), 'r') as f:
        index = f.read()
        f.close()

    with open(os.path.join("Xblog", "docs", "index.html"), 'w') as f:
        index = index.replace(nav, new_nav.replace('${Xbook/Xpage}$', title).replace('${link}$', "notebooks/"+title+"/index.html"))
        f.write(index)
        f.close()
    ccc.success("adding " + title + " to navigation pallete")


def addToParentIndex(des, tipe):
    """
    adds Xpage or Xbook on parent's index
    """
    title = des.split(os.path.sep)[-1].replace(".html", "")
    index = des.replace(os.path.basename(des), "index.html")
    band = "<!-- $band$ -->"
    bands = [
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(24, 26, 27) ;'><th scope = 'row' style = ' border-color: rgb(128, 111, 105) ;' >$Subject$</th><td style = '  border-color: rgb(128, 111, 105) ;' >$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(17, 17, 34) ;'><th scope='row' style='border-color: rgb(109, 145, 145) ;'>$Subject$</th><td style='border-color: rgb(109, 145, 145) ;'>$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(17, 26, 34) ; '><th scope='row' style='  border-color: rgb(70, 104, 140) ;'>$Subject$</th><td style='  border-color: rgb(70, 104, 140) ;'>$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(14, 37, 21) ; '><th scope='row' style='  border-color: rgb(55, 157, 85) ;'>$Subject$</th><td style=' border-color: rgb(55, 157, 85) ;'>$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(43, 41, 8) ; '><th scope='row' style='  border-color: rgb(198, 187, 26) ;'>$Subject$</th><td style='  border-color: rgb(198, 187, 26) ;'>$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(43, 26, 8) ; '><th scope='row' style='  border-color: rgb(193, 109, 24) ;'>$Subject$</th><td style='border-color: rgb(193, 109, 24) ;'>$Description$</td></tr><!-- $band$ -->",
                "<tr onclick=\"window.location.replace(\'$link$\')\" style='background-color: rgb(41, 11, 10) ; '><th scope='row' style='  border-color: rgb(199, 39, 34) ;'>$Subject$</th><td style='border-color: rgb(199, 39, 34) ;'>$Description$</td></tr><!-- $band$ -->"
            ]

    with open(index, 'r') as f:
        body = f.read()
        f.close()

    with open(index, 'w') as f:
        body = body.replace('$title$', 'TOC of ' + des.replace(des.split(os.path.sep)[-1], "")).replace('$bootstrap.css$', os.path.join("/", "Assets", "css", "bootstrap.css")).replace('$index.css$', os.path.join("/", "Assets", "css", "index.css"))
        body = BeautifulSoup(body.replace(band, bands[0].replace('$Subject$', title).replace('$Description$', "it's my way of thinkinng!!").replace('$link$', title+'.html')), 'html.parser').prettify()
        f.write(body)
        f.close()
    ccc.success("adding " + des + " to parent index")


def install(des, tipe):
    """
    called at every creation of Xbook or Xpage
    """
    print(des)
    if tipe == "Xbook":
        src = os.path.join("Xblog", "docs", "Assets", "html", "index.html")
        shutil.copy2(src, des)
        ccc.success("installing index of " + des)
        if des.replace(os.path.basename(des), "") == os.path.join("Xblog", "docs", "notebooks") + "\\":
            addToNavBar(des, tipe)
        else:
            addToParentIndex(des, tipe)

    if tipe == "Xpage":
        linkAssets(des)
        if des.replace(os.path.basename(des), "") == os.path.join("Xblog", "docs", "notebooks") + "\\":
            if not des.endswith("welcome.html"):
                addToNavBar(des, tipe)
        else:
            addToParentIndex(des, tipe)
    ccc.success("installtion procedures for " + des)