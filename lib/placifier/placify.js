#!/usr/bin/env node

'use strict';

const fs = require('fs');
const path = require('path');

const ccc = require('../common_cli_conventions');

function rootIndex_html(Xrc) {
    let des = path.join(path.resolve(), "docs", "index.html");
    fs.readFile(
        des,
        (err, data) => {
            if (err) process.exit(ccc.fail(err))
            else {
                ccc.success("fetching " + des)
                fs.writeFile(
                    des,
                    String(data)
                    .replace("$TITLE$", Xrc["blog_name"] || "")
                    .replace(/\$REPO\$/g, Xrc["gh_repo_name"] || "")
                    .replace(/\$AUTHOR\$/g, Xrc["Author_name"] || "")
                    .replace("$PEN$", Xrc["Pen_name"] || "")
                    .replace("$KEYWORDS$", Xrc["keywords"] || "")
                    .replace(/\$BOLG_DESCRIPTION\$/g, Xrc["blog_description"] || "")
                    .replace("$GH$", "https://github.com/" + Xrc["GitHub_Username"] || "")
                    .replace("$EMAIL$", Xrc["Email"] || ""),
                    err => {
                        if (err) process.exit(ccc.fail(err));
                        else ccc.success("placifying " + des)
                    }
                );
            }
        }
    );
}

function subIndex_html(Xrc) {
    let des = path.join(path.resolve(), "docs", "Assets", "html", "index.html");
    fs.readFile(
        des, 
        (err, data) => {
            if (err) process.exit(ccc.fail(err));
            else {
                ccc.success("fetching " + des);
                fs.writeFile(
                    des,
                    String(data)
                        .replace("$TITLE$", Xrc["blog_name"])
                        .replace(/\$REPO\$/g, Xrc["gh_repo_name"]),
                    err => {
                        if(err) process.exit(ccc.fail(err));
                        else ccc.success("placifying " + des)
                    }
                );
            }
        }
    );
}

function rootIndex_css(Xrc){
    let des = path.join(path.resolve(), "docs", "Assets", "css", "root_index.css");

    fs.readFile(
        des,
        (err, data)=>{
            if(err) process.exit(ccc.fail(err));
            else{
                ccc.success("fetching " + des);
                fs.writeFile(
                    des,
                    String(data)
                        .replace(/\$REPO\$/g, Xrc["gh_repo_name"]),
                    err=>{
                        if(err) process.exit(ccc.fail(err))
                        else ccc.success("placifying "+ des)
                    } 
                )
            }
        }
    )
}

function mobile_html(Xrc){
    let des = path.join(path.resolve(), "docs", "Assets", "html", "Xbooks_mobile.html");

    fs.readFile(
        des,
        (err, data)=>{
            if(err) process.exit(ccc.fail(err))
            else{
                ccc.success("fetching " + des);
                fs.writeFile(
                    des,
                    String(data)
                        .replace(/\$REPO\$/g, Xrc["gh_repo_name"]),
                    err=>{
                        if(err) process.exit(ccc.fail(err))
                        else ccc.success("placifying " + des)
                    }
                )
            }
        }
    )
}

function welcome_html(Xrc){
    let des = path.join(path.resolve(), "docs", "notebooks", "welcome.html");
    
    fs.readFile(
        des,
        (err, data)=>{
            if(err) process.exit(ccc.fail(err))
            else{
                ccc.success("fetching " + des);
                fs.writeFile(
                    des,
                    String(data)
                        .replace(/\$REPO\$/g, Xrc["gh_repo_name"]),
                    err=>{
                        if(err) process.exit(ccc.fail(err));
                        else ccc.success("placifying " + des)
                    }
                )
            }
        }
    )
}

module.exports = {
    placify: () => {
        if (fs.existsSync(".Xbooksrc")) {
            if (fs.existsSync(path.resolve(), "docs", "Xtheme.json")) {

                let Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'));
                ccc.success("reading .Xbooksrc")

                rootIndex_html(Xrc);
                subIndex_html(Xrc);
                rootIndex_css(Xrc);
                mobile_html(Xrc);
                welcome_html(Xrc);
            } else {
                ccc.fail("kindly first install Xbooks dependency source by running...")
                ccc.code([
                    "Xbooks install"
                ])
            }
        } else ccc.fail("this is not an Xbooks project!")
    }
}