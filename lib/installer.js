#!/usr/bin/env node

'use strict';

const fs = require("fs");
const path = require("path");
const fse = require('fs-extra');

const ccc = require("../lib/common_cli_conventions.js");

const copy_file = (src, des) => {
    fs.createReadStream(src)
      .pipe(fs.createWriteStream(des)).on('error', (err) => {
          console.error(err);
      });
    ccc.success("installing " + path.basename(src))
};

const copy_dir = (src, des) => {
    fse.copy(src, des, (err) => {
        if (err) return console.error(err);
        ccc.success('installing ' + path.basename(src));
    });
};

const install_CI = (src_root, des_root, CI) => {
    switch (CI) {
        case "GitLabCI":
            copy_file(path.resolve(src_root, "CI", "GitLabCI", ".gitlab-ci.yml"), path.resolve(des_root, ".gitlab-ci.yml"))
            break;

        case "CircleCI":
            break;

        case "TravisCI":
            break;

        case "other":
            ccc.fail("kindly head over to documentation of the CI platform you're using and pipeline this repo/blog \nby writing a config file for your platform as described in the Xbooks documentation!");
            break;
    }
};

const install_Xtheme = (src_root, des_root, Xtheme) => {
    copy_dir(path.resolve(src_root, "themes", Xtheme), path.resolve(des_root, "docs"));
};


module.exports = {

    install: (src_root, des_root) => {
        if(! fs.existsSync('.Xbooksrc')){
            ccc.fail(".Xbooksrc doesn't exist!");
        }
        else{
                this.Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'))
                ccc.success("reading .Xbooksrc")
                install_CI(src_root, des_root, this.Xrc.CI);
                install_Xtheme(src_root, des_root, this.Xrc.Xtheme);
        }
    },


}