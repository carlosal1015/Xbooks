#!/usr/bin/env python

import os, sys
import shutil
from bs4 import BeautifulSoup
import time, datetime
import shutil

from .import ccc, e, cnv

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


def rename(tbr, tipe):
    """
    renames Xpage or Xbook and returns True if success; False otherwise
    """
    src = tbr[0].replace(".ipynb", ".html")
    des = tbr[1].replace(".ipynb", ".html")
    os.renames(os.path.join("Xblog/docs", src), os.path.join("Xblog/docs", des))
    ccc.success("renaming " + src + " to " + des)
    update(src, des, tipe)
    src_pdf = tbr[0].replace(".ipynb", ".pdf").replace("notebooks", "pdfs")
    des_pdf = tbr[1].replace(".ipynb", ".pdf").replace("notebooks", "pdfs")
    os.renames("Xblog/docs/" + src_pdf, "Xblog/docs/" + des_pdf)
    ccc.success("renaming " + src_pdf + " to " + des_pdf)
    if tbr[0] == "notebooks/welcome.ipynb":
        if os.path.isfile("Xblog/README.md"):
            cnv.md2html()
        else:
            with open("Xblog/docs/notebooks/welcomme.html", 'w') as f:
                f.write("<html>\n<body>\n<h1 align=\"center\">Welcome to Xbooks blogs!</h1>\n<h4 align=\"center\">This blog has no welcome page<br/>if you're maintainer of this blog, kindly write either README.md or notebooks/welcome.ipynb file!</h4>\n</body>\n</html>\n")
                f.close()
    return True

def delete(tbd, tipe):
    """
    deletes and returns True if success; False otherwise
    """
    des = "Xblog/docs/" + tbd.replace(".ipynb", ".html")
    uninstall(des)
    if tipe == "Xpage":
        os.remove(des)
        ccc.success("deleting " + des)
        des_pdf = des.replace(".html",".pdf").replace("notebooks", "pdfs")
        os.remove(des_pdf)
        ccc.success("deleting " + des_pdf)
        if tbd == "notebooks/welcome.ipynb":
            if os.path.isfile("Xblog/README.md"):
                cnv.md2html()
            else:
                with open("Xblog/docs/notebooks/welcomme.html", 'w') as f:
                    f.write("<html>\n<body>\n<h1 align=\"center\">Welcome to Xbooks blogs!</h1>\n<h4 align=\"center\">This blog has no welcome page<br/>if you're maintainer of this blog, kindly write either README.md or notebooks/welcome.ipynb file!</h4>\n</body>\n</html>\n")
                    f.close()
    if tipe == "Xbook":
        shutil.rmtree(des)
        ccc.success("deleting " + des)
    return True


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


def addToParentIndex(des, tipe, Xrc):
    """
    adds Xpage or Xbook on parent's index
    """
    title = des.split("/")[-1].replace(".html", "")
    index = des.replace(os.path.basename(des), "index.html")
    with open(index, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        f.close()
    with open(index, 'w') as f:
        notebook = "/".join(des.split("/")[2:])
        soup.head.title.string = 'TOC of ' + des.replace(des.split("/")[-1])
        if tipe == "Xpage":
            tr = soup.new_tag('tr')
            tr["id"] = title
            tr["onclick"] = "window.location.replace('$LINK$'); updateExplorer_IFrame('$LINK$')".replace("$LINK$", '\\\\' + Xrc["gh_repo_name"] + '/' + notebook)
            tr["style"] = "background-color: rgb(55, 57, 58); width: 100vw; box-shadow: gray 2px 2px 2px;"
            th = soup.new_tag('th')
            th["scope"] = "row"
            th["style"] = "border: none; width: 60vw;"
            th.string = title
            td = soup.new_tag('td')
            td["style"] = "border: none; width: 40vw;"
            td.string = datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M.%S|$MONTH$ %d %Y by Xbooks[bot]").replace("$MONTH$", chooseMonth(datetime.datetime.fromtimestamp(time.time()).strftime("%m")))
            tr.insert(0, td)
            tr.insert(0, th)
            soup.body.select('table')[1].tbody.insert(0, tr)
        if tipe == "Xbook":
            notebook = notebook + "/index.html"
            shutil.copy2(des.replace("docs/", "") + "/card.png", des + "/card.png")
            ccc.note("copied " + des.replace("docs/", "") + "/card.png to" + des + "/card.png")
            td = soup.new_tag('td')
            td["id"] = title
            div_wrapper = soup.new_tag('div')
            div_wrapper["onclick"] = "window.location.replace('$LINK$'); updateExplorer_IFrame(\'$LINK$\');".replace("$LINK$", '\\\\' + Xrc["gh_repo_name"] + '/' + notebook)
            div_wrapper["class"] = "card bg-light mb-3"
            div_wrapper["style"] = "max-width: 20rem; background-color: rgba(39, 39, 39, 0.819) !important; color: rgb(200, 192, 188) !important; border: none; box-shadow: gray 5px 5px 5px;"
            div_head = soup.new_tag('div')
            div_head["class"] = "card-header"
            div_head["style"] = "background-color: rgba(37, 37, 37, 0.877) !important; border: none; color: white;"
            div_head.string = title
            div_wrapper.insert(0, div_head)
            if os.path.exists(des.replace("docs/", "") + "/card.png"):
                div_body = soup.new_tag('div')
                div_body["class"] = "card-body"
                img = soup.new_tag('img')
                img["style"] = "height: 256px; width: 256px; display: block; filter: saturate(0.7) brightness(0.5);"
                img["src"] = title+"/card.png"
                div_body.insert(0, img)
                div_wrapper.insert(-1, div_body)
            td.insert(0, div_wrapper)
            if len(soup.table.tr.select("td")) == 3:
                tr = soup.new_tag('tr')
                soup.table.insert(0, tr)
            soup.table.tr.insert(0, td)
        f.write(soup)
        f.close()
    ccc.success("adding " + des + " to parent index")

def install(des, tipe):
    """
    called at every creation of Xbook or Xpage
    """
    from xbooks.Xinit import Xrc
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


def removeFromNavBar(des):
    """
    removes Xbook or Xpage from navbar
    """
    index = "Xblog/docs/index.html"
    title = des.split("/")[-1].replace(".html", "")
    with open(index, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        f.close()
    soup.select("#"+title)[0].decompose()
    with open(index, 'w') as f:
        f.write(soup.prettify(formatter="html"))
        f.close()
    ccc.success("removing " + des + " from navigation pallete")

def removeFromParentIndex(des):
    """
    removes Xbook or Xpage from parent's index
    """
    index = des.replace(os.path.basename(des), "index.html")
    title = des.split("/")[-1].replace(".html", "")
    with open(index, "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        f.close()
    soup.select("#"+title)[0].decompose()
    with open(index, "w") as f:
        f.write(soup.prettify(formatter="html"))
        f.close()
    ccc.success("removing " + des + " from parent index")

def uninstall(des):
    """
    called at every removal of Xbook or Xpage
    """
    if "Xblog/docs/notebooks/" == des.replace(os.path.basename(des), ""):
        removeFromNavBar(des)
    else:
        removeFromParentIndex(des)
    ccc.success("uninstallation procedures for " + des)

def editNavBar(src, des, tipe, Xrc):
    """
    edits Xbook or Xpage on navbar
    """
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


def editParentIndex(src, des, tipe, Xrc):
    """
    edits Xbook or Xpage on parent's index
    """
    old_title = src.split("/")[-1].replace(".html", "")
    new_title = des.split("/")[-1].replace(".html", "")
    index = des.replace(os.path.basename(des), "index.html")
    with open(index, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        f.close()
    tag = soup.select("#"+old_title)[0]
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


def update(src, des, tipe):
    """
    called at every rename of Xbook or Xpage
    """
    from xbooks.Xinit import Xrc
    src = "Xblog/docs/" + src
    des = "Xblog/docs/" + des
    if "Xblog/docs/notebooks/" == des.replace(os.path.basename(des), ""):
        editNavBar(src, des, tipe, Xrc)
    else:
        editParentIndex(src, des, tipe, Xrc)
    ccc.success("updatation procedures for " + des)
