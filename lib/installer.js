#!/usr/bin/env node

'use strict';

const fs = require("fs");
const fse = require("fs-extra");
const path = require("path");

const ccc = require("./common_cli_conventions");

module.exports = {

    install: (src_root, des_root) => {
        if (!fs.existsSync('.Xbooksrc')) {
            ccc.fail(".Xbooksrc doesn't exist!");
        } else {
            this.Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'))
            ccc.success("reading .Xbooksrc")

            fse.copy(path.resolve(src_root, "src", "themes", this.Xrc.Xtheme), path.resolve(des_root, "docs"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ this.Xrc.Xtheme);
            });
            fse.copy(path.resolve(src_root, "src", "etc", "ref.bib"), path.resolve(des_root, "ref.bib"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ "ref.bib");
            });
            fse.copy(path.resolve(src_root, "src", "etc", "template.tplx"), path.resolve(des_root, "template.tplx"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ "template.tplx");
            });
            fse.copy(path.resolve(src_root, "src", "etc", ".gitpod.yml"), path.resolve(des_root, ".gitpod.yml"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ ".gitpod.yml");
            });
            fse.copy(path.resolve(src_root, "src", "etc", ".gitpod.dockerfile"), path.resolve(des_root, ".gitpod.dockerfile"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ ".gitpod.dockerfile");
            });
            fse.copy(path.resolve(src_root, "src", "etc", "environment.yml"), path.resolve(des_root, "environment.yml"), err => {
                if(err) return console.error(err);
                ccc.success("installing "+ "environment.yml");
            });
            switch (this.Xrc.CI) {
                case "GitLabCI":
                    fse.copy(path.resolve(src_root, "src", "CI", "GitLabCI", ".gitlab-ci.yml"), path.resolve(".gitlab-ci.yml"), err => {
                        if(err) return console.error(err);
                        ccc.success("installing "+ ".gitlab-ci.yml");
                    })
                    break;

                case "CircleCI":
                    fse.copy(path.resolve(src_root, "src", "CI", "CircleCI", ".circleci"), path.resolve(".circleci"), err => {
                        if(err) return console.error(err);
                        ccc.success("installing "+ ".circleci/config.yml");
                    })
                    break;

                case "TravisCI":
                    fse.copy(path.resolve(src_root, "src", "CI", "TravisCI", ".travis.yml"), path.resolve(".travis.yml"), err => {
                        if(err) return console.error(err);
                        ccc.success("installing "+ ".travis.yml");
                    })
                    break;

                case "other":
                    ccc.fail("kindly head over to documentation of the CI platform you're using and pipeline this repo/blog \nby writing a config file for your platform as described in the Xbooks documentation!");
                    break;
            }
            ccc.note("create one PAT for xbooks pipeline from GitHub and two environment variables in your CI Platform runner as following ...");
            ccc.code([
                "GH_REPO: <your github repo url> (e.g. https://github.com/{USERNAME/ORGNAME}/{REPONAME}.git)",
                "GH_PAT: <the token you created on github> (a string of 40 characters)"
            ], true);
        }
    }
}