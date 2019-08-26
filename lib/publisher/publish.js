#!/usr/bin/env node

'use strict';

const ccc = require("../common_cli_conventions");

const inquirer = require("inquirer")
const fs = require("fs")
const path = require("path");
const git = require("simple-git")(path.resolve())

git.silent(true);

function add_commit_pusher(data){

    let UNAME;
    let RNAME;
    let NAMESPACE;
    let STAT;

    UNAME = data["GitHub_Username"];
    RNAME = data["gh_repo_name"];
    NAMESPACE = data["gh_repo_namespace"]
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
                                    git.push(`https://${UNAME}:${res["PASSKEY"]}@github.com/${NAMESPACE}/${RNAME}.git`, "master", err => {
                                        if (err) process.exit(ccc.fail(err))
                                        else {
                                            ccc.success("pushing! ")
                                            ccc.note("if you've enable GitHub Pages for /docs folder you'd get your output on")
                                            ccc.blue("URL", `https://${NAMESPACE}.github.io/${RNAME}`);
                                            ccc.note("if everything goes well on the pipeline side!; check the status there if needed.")
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
            ccc.note("kindly, (if not already) first install Xbooks dependancies source by running...");
            ccc.code([
                "Xbooks install",
                "Xbooks placify"
            ]);
            ccc.note("checking and pushing if any unpushed commits exists");
            inquirer.prompt({
                type: "password",
                name: "PASSKEY",
                message: `PassKey for GitHub.com/${data["GitHub_Username"]}`
            }).then((res) => {
                ccc.note("plz wait while pushing unpushed commits(if existed)...");
                git.push(`https://${UNAME}:${res["PASSKEY"]}@github.com/${NAMESPACE}/${RNAME}.git`, "master", err => {
                    if (err) process.exit(ccc.fail(err))
                    else {
                        ccc.success("pushing unpushed commits (if existed)");
                        ccc.note("if you've enable GitHub Pages for /docs folder you'd get your output on");
                        ccc.blue("URL", `https://${NAMESPACE}.github.io/${RNAME}`);
                        ccc.note("if everything goes well on the pipeline side!; check the status there if needed.");
                    }
                })
            })
        }
    })
}

module.exports = {
    publish: (opt) => {
        if (opt) {
            fs.readFile(".Xbooksrc", (err, data) => {
                if(err){
                    ccc.alert("this is not an Xbooks project");
                    ccc.note("try running...");
                    ccc.code([
                        "Xbooks init",
                        "Xbooks install",
                        "Xbooks placify"
                    ]);
                    ccc.note("and then run this command to publish!");
                    process.exit(ccc.fail(err));
                }
                else {
                    ccc.success("reading .Xbooksrc");
                    add_commit_pusher(JSON.parse(data));
                }
            })
        }
        else{
            fs.readFile(".Xbooksrc", (err, data)=>{
                if(err){
                    ccc.alert("this is not an Xbooks project");
                    ccc.note("try running...");
                    ccc.code([
                        "Xbooks init",
                        "Xbooks install",
                        "Xbooks placify"
                    ]);
                    ccc.note("and then run this command to publish!");
                    process.exit(ccc.fail(err))
                }
                else{
                    data = JSON.parse(data);
                    ccc.success("reading Xbooksrc");
                    git.pull(`https://github.com/${data["gh_repo_namespace"]}/${data["gh_repo_name"]}.git`, "master", (err, ups)=>{
                        if(err){
                            ccc.note("if this is first time you're publishing this Xbooks project, try runnning...");
                            ccc.code([
                                "Xbooks publish -i"
                            ]);
                            ccc.alert("or check if your repo actually exists on GitHub.com by the name you specified;\nto check Xbooks configurations open .Xbooksrc file");
                            process.exit(ccc.fail(err));
                        }
                        else {
                            ccc.success(`pulling from remote https://github.com/${data["gh_repo_namespace"]}/${data["gh_repo_name"]}.git master`);
                            ccc.blue("Updates", JSON.stringify(ups, null, "  "));
                            add_commit_pusher(data);
                        }
                    })
                }
            })
        }
    }
}