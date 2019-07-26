#!/usr/bin/env node

'use strict';

const rimraf = require("rimraf");
const ccc = require("../common_cli_conventions");

module.exports = {
    uninstall: (opt) => {
        ccc.note("if following files existed ...")
        rimraf("docs/", () => {
            ccc.success("uninstalling docs/")

            rimraf(".gitlab-ci.yml", () => {
                ccc.success("uninstalling .gitlab-ci.yml")
                rimraf(".circleci", () => {
                    ccc.success("uninstalling .circleci");
                    if(!opt)
                    ccc.success("partially uninstalling Xbooks");
                    if(opt) rimraf(".Xbooksrc", ()=>{
                        ccc.success("uninstalling .Xbooksrc");
                        ccc.success("fully uninstalling Xbooks");
                    }, (err)=>{
                        ccc.fail("uninstalling .Xbooksrc")
                    })
                }, (err) => {
                    if (err) {
                        ccc.fail("uninstalling .circleci");
                    }
                });
            }, (err) => {
                if (err) ccc.fail("uninstalling .gitlab-ci.yml");
            });
        }, (err) => {
            if (err) ccc.fail("uninstalling docs/")
        });
    }
}