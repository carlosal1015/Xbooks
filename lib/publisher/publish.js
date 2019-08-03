#!/usr/bin/env node

'use strict';

const ccc = require("../common_cli_conventions");

const inquirer = require("inquirer")
const fs = require("fs")
const path = require("path");
const git = require("simple-git")(path.resolve())

git.silent(true);

module.exports = {
    publish: (opt) => {
        if (opt) {
            let UNAME;
            let RNAME;
            let STAT;
            fs.readFile(".Xbooksrc", (err, data) => {
                if (err) process.exit(ccc.fail(err))
                else {
                    ccc.success("reading .Xbooksrc");
                    data = JSON.parse(data)
                    UNAME = data["GitHub_Username"];
                    RNAME = data["gh_repo_name"];
                    git.status((err, stat) => {
                        if (err) process.exit(ccc.fail(err))
                        else {
                            STAT = stat;
                            ccc.blue("Status", JSON.stringify(stat, null, "  "))
                        }
                    }).exec(() => {
                        if (STAT["files"].length) {
                            inquirer.prompt({
                                type: "confirm",
                                name: "CNF",
                                message: "good to go??"
                            }).then(res => {
                                if (res["CNF"]) {
                                    git.add("./*", err => {
                                        if (err) process.exit(ccc.fail(err))
                                        else ccc.success("addding unstaged files(if existed) to stagging stack")
                                    }).exec(() => {
                                        inquirer.prompt({
                                            type: "input",
                                            message: "type commit message",
                                            name: "CM",
                                            default: ()=>{
                                                return "initial blast!"
                                            }
                                        }).then(res => {
                                            git.commit(res["CM"], err => {
                                                if (err) process.exit(ccc.fail(err))
                                                else ccc.success("commiting!")
                                            }).exec(() => {
                                                inquirer.prompt({
                                                    type: "password",
                                                    name: "PASSKEY",
                                                    message: `PassKey for GitHub.com/${data["GitHub_Username"]}`
                                                }).then((res) => {
                                                    ccc.note("plz wait while pushing...")
                                                    git.push(`https://${UNAME}:${res["PASSKEY"]}@github.com/${UNAME}/${RNAME}.git`, "master", err => {
                                                        if (err) process.exit(ccc.fail(err))
                                                        else {
                                                            ccc.success("pushing! ")
                                                            ccc.blue("URL", `https://${UNAME}.github.io/${RNAME}`)
                                                        }
                                                    })
                                                })
                                            })
                                        })
                                    })
                                }
                            })
                        } else {
                            ccc.alert("nothing to commit!");
                            ccc.note("kindly, first install Xbooks dependancies source by running...");
                            ccc.code([
                                "Xbooks install",
                                "Xbooks placify"
                            ]);
                        }
                    })
                }
            })
        }
    }
}