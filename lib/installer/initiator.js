#!/usr/bin/env node

'use strict';

const fs = require("fs");
const path = require("path");
const fse = require('fs-extra');

const ccc = require("../common_cli_conventions");

const CI_installer = require("./CI_installer");
const theme_installer = require("./theme_installer");

module.exports = {

    install: (src_root, des_root) => {
        if(! fs.existsSync('.Xbooksrc')){
            ccc.fail(".Xbooksrc doesn't exist!");
        }
        else{
                this.Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'))
                ccc.success("reading .Xbooksrc")
                CI_installer.install(src_root, des_root, this.Xrc.CI);
                theme_installer.install(src_root, des_root, this.Xrc.Xtheme);
        }
    }
}