#!/usr/bin/env node

'use strict';

const fs = require("fs");
const path = require("path");
const copier = require("./copier");


const ccc = require("../common_cli_conventions");

module.exports = {

    install: (src_root, des_root) => {
        if (!fs.existsSync('.Xbooksrc')) {
            ccc.fail(".Xbooksrc doesn't exist!");
        } else {
            this.Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'))
            ccc.success("reading .Xbooksrc")
            
            copier.copy_dir(path.resolve(src_root, "src", "themes", this.Xrc.Xtheme), path.resolve(des_root, "docs"));

            switch (this.Xrc.CI) {
                case "GitLabCI":
                    copier.copy_file(path.resolve(src_root, "src", "CI", "GitLabCI", ".gitlab-ci.yml"), path.resolve(des_root, ".gitlab-ci.yml"))
                    break;

                case "CircleCI":
                    copier.copy_dir(path.resolve(src_root, "src", "CI", "CircleCI", ".circleci"), path.resolve(des_root, ".circleci"))
                    break;

                case "other":
                    ccc.fail("kindly head over to documentation of the CI platform you're using and pipeline this repo/blog \nby writing a config file for your platform as described in the Xbooks documentation!");
                    break;
            }
            ccc.note("create one PAT for xbooks pipeline from GitHub and two environment variables in your CI Platform runner as following ...");
            ccc.code([
                "REPO_URL: <your github repo url> (e.g. https://github.com/{USERNAME/ORGNAME}/{REPONAME}.git)",
                "GH_TOKEN: <the token you created on github> (a string of 40 characters)"
            ]);
        }
    }
}