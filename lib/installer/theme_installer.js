#!/usr/bin/env node

'use strict';

const copier = require("./copier");
const path = require("path");
const fs = require("fs");

function calltocopy(src_root, des_root, Xtheme){
    copier.copy_dir(path.resolve(src_root, "src", "themes", Xtheme), path.resolve(des_root, "docs"));
    return true
}

function calltoread(){
    let index = path.join(path.resolve(), "docs", "index.html");
    fs.readFile(index, 'utf8', (err, body) => {
        if (err) console.error(err)
        return body
    });
}

module.exports = {
    install: (src_root, des_root, Xtheme) => {
        // edit root index.html by replacing placeholders with the data of user from xbooksrc
        let res = undefined
        while(!res){
            res = calltocopy(src_root, des_root, Xtheme);
        }
        console.log(res);
        calltoread();
    }
}