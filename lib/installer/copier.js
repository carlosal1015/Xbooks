#!/usr/bin/env node

'use strict';

const ccc = require("../common_cli_conventions");

const fs = require("fs");
const fse = require("fs-extra");
const path = require("path");

module.exports = {
    copy_file : (src, des) => {
        if(! fs.existsSync(des)){
            fs.createReadStream(src)
            .pipe(fs.createWriteStream(des)).on('error', (err) => {
                console.error(err);
            }).on("close", ()=>{
                ccc.success("installing " + path.basename(src));
                return true;
            });
        }
        else{
            ccc.note(des + " exists already!");
        }
    },

    copy_dir : (src, des) => {
        if(! fs.existsSync(des)){
            fse.copy(src, des, (err) => {
                if (err) return console.error(err);
                ccc.success('installing ' + path.basename(src));
            });
        }
        else{
            ccc.note(des + " exists already!")
        }
    }
}