#!/usr/bin/env node

'use strict';

const copier = require("./copier");
const ccc = require("../ccc/common_cli_conventions");
const path = require("path");

module.exports = {
    install: (src_root, des_root, CI) => {
    switch (CI) {
        case "GitLabCI":
            copier.copy_file(path.resolve(src_root, "src", "CI", "GitLabCI", ".gitlab-ci.yml"), path.resolve(des_root, ".gitlab-ci.yml"))
            break;

        case "CircleCI":
            break;

        case "TravisCI":
            break;

        case "other":
            ccc.fail("kindly head over to documentation of the CI platform you're using and pipeline this repo/blog \nby writing a config file for your platform as described in the Xbooks documentation!");
            break;
        }
    }
}