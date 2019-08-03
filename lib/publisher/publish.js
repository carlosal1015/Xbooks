#!/usr/bin/env node

'use strict';

const ccc = require("../common_cli_conventions");

const inquirer = require("inquirer")
const fs = require("fs")
const path = require("path");
const git = require("simple-git")()

module.exports = {
    publish: () => {
        if (fs.existsSync(".Xbooksrc")) {
            if (fs.existsSync(path.resolve(), "docs", "Xtheme.json")) {
                let Xrc = JSON.parse(fs.readFileSync('.Xbooksrc'));
                ccc.success("reading .Xbooksrc");

                let repo = `https://github.com/${Xrc["GitHub_Username"]}/${Xrc["gh_repo_name"]}.git`

                git.pull(repo || 'origin', "master", (err, updates) => {
                    if (err) {
                        if (!(String(err).includes("remote") && String(err).includes("ref") && String(err).includes("master")))
                        process.exit(ccc.fail(err));
                        else
                        ccc.note("there's nothing on remote to pull!");
                    } else {
                        ccc.success("pulling from remote")
                        ccc.blue("Updates", updates.summary)
                    }
                }).exec(() => {
                    git.push(repo || 'origin', 'master', err => {
                        if (err) {
                            if (!String(err).includes("master"))
                                process.exit(ccc.fail(err))
                            else
                                ccc.note("there's no unpushed commits!");
                        } else
                            ccc.success("checking and pushing unpushed commits!");
                    }).exec(() => {
                        git.add("./*", err => {
                            if (err) process.exit(ccc.fail(err))
                            else {
                                ccc.success("adding unstaged files(if there were any) to stagging stack!");
                                inquirer.prompt({
                                    type: "editor",
                                    message: "type commit message",
                                    name: Commit_message
                                }).then((res) => {
                                    git.commit(res["Commit_message"], err => {
                                        if (err) process.exit(cc.fail(err))
                                        else {
                                            ccc.success("commiting with message...")
                                            ccc.blue("Commit Message", Commit_message)
                                        }
                                    }).exec(() => {
                                        git.push(repo || 'origin', 'master', err => {
                                            if (err) process.exit(ccc.fail(err))
                                            else ccc.success("pushing to remote!")
                                        })
                                    })
                                }).catch(err => process.exit(ccc.fail(err)))
                            }
                        })
                    })
                })
            } else {
                ccc.fail("kindly first install Xbooks dependency source by running...")
                ccc.code([
                    "Xbooks install"
                ])
            }
        } else ccc.fail("this is not an Xbooks project!")
    }
}