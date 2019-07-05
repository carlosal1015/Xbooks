#!/usr/bin/env node

'use strict';

const copier = require("./copier");
const path = require("path");

module.exports = {
    install: (src_root, des_root, Xtheme) => {
    copier.copy_dir(path.resolve(src_root, "src", "themes", Xtheme), path.resolve(des_root, "docs"));
    }
}