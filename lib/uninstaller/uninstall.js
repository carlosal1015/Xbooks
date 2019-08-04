#!/usr/bin/env node

'use strict';

const rimraf = require("rimraf");
const inquirer = require("inquirer");

const ccc = require("../common_cli_conventions");

module.exports = {
    uninstall: (opt) => {
        inquirer.prompt({
            type: "confirm",
            name: "CNF",
            message: "Are you Aware of what's going on here??"
        }).then(res => {
            if (res["CNF"]) {
                ccc.note("if following files existed ...")
                rimraf("docs/", () => {
                    ccc.success("uninstalling docs/")
                    rimraf(".gitlab-ci.yml", () => {
                        ccc.success("uninstalling .gitlab-ci.yml")
                        rimraf(".circleci", () => {
                            ccc.success("uninstalling .circleci");
                            rimraf(".git", ()=>{
                               ccc.success("removing git refs");
                               if (!opt)
                                   ccc.success("partially uninstalling Xbooks");
                               if (opt) rimraf(".Xbooksrc", () => {
                                   ccc.success("uninstalling .Xbooksrc");
                                   ccc.success("fully uninstalling Xbooks");
                               }, err => {
                                   process.exit(ccc.fail(err))
                               })
                            }, err=>{
                                if(err) ccc.fail("removing git refs");
                            })
                        }, err => {
                            if (err) {
                                ccc.fail("uninstalling .circleci");
                            }
                        });
                    }, err => {
                        if (err) ccc.fail("uninstalling .gitlab-ci.yml");
                    });
                }, err => {
                    if (err) ccc.fail("uninstalling docs/")
                });
            }
        }).catch(err => {
            if (err) process.exit(ccc.fail(err));
        })
    }
}