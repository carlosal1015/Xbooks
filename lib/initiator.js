#!/usr/bin/env node

'use strict';

const inquirer = require('inquirer');
const fs = require('fs');
const path = require('path');
const git = require('simple-git')(path.resolve());

const ccc = require('../lib/common_cli_conventions');

const rcfile_name = ".Xbooksrc";
const Xbooks_root = path.join(process.argv[1].replace(path.join("bin","Xbooks.js"), ""));

const blank_rc = {
    "blog_name": "",
    "Author_name": "",
    "Pen_name": "blong ",
    "Email": "",
    "Website": "",
    "phone": "",
    "GitHub_Username": "",
    "GitHub_repo_name": "",
    "biodata": "",
    "blog_description": "",
    "CI": "",
    "Xtheme": "",
    "JNbooks": "",
    "Xbooks": ""
  }

const getlist = (filepath)=>{
    if(fs.existsSync(filepath))
    return fs.readFileSync(filepath).toString().split('\n');
    else return ""
}

var questions = [
    {
        type: 'input',
        name: 'blog_name',
        message: "Blog's name:"
    },
    {
        type: 'input',
        name: 'Author_name',
        message: "Author's name(formal or real name):"
    },
    {
        type: 'input',
        name: 'Pen_name',
        message: "Author's name(informal or pen-name):"
    },
    {
        type: 'input',
        name: 'Email',
        message: "Author's Email:"
    },
    {
        type: 'input',
        name: 'Website',
        message: "Author's Website:"
    },
    // {
    //     type: 'input',
    //     name: 'phone',
    //     message: "What's your phone number",
    //     validate: function (value) {
    //         var pass = value.match(
    //             /^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$/i
    //         );
    //         if (pass || value=="") {
    //             return true;
    //         }

    //         return 'Please enter a valid phone number';
    //     }
    // },
    {
        type: 'input',
        name: 'GitHub_Username',
        message: "Author's GitHub.com Username/Orgname:"
    },
    {
        type: 'input',
        name: 'gh_repo_name',
        message: "blog's GitHub repo name:"
    },
    {
        type: 'list',
        name: 'CI',
        message: "which CI platform you want to use?",
        choices: ()=>{
            let list = [];
            list = getlist(path.join(Xbooks_root, 'src', 'CI', 'CI.list'));
            list.push("other");
            return list;
        }
    },
    {
        type: 'list',
        name: 'Xtheme',
        message: "which Xtheme you want to use?",
        choices: getlist(path.join(Xbooks_root, 'src', 'themes', 'themes.list'))
    },
    // {
    //     type: 'list',
    //     name: 'Xplugin',
    //     message: "which Xplugin you want to use?",
    //     choices: ()=>{
    //         let list = [];
    //         list = getlist(path.join(Xbooks_root, 'src', 'plugins', 'plugins.list'));
    //         list.push("None");
    //         return list;
    //     }
    // },
    // {
    //     type: 'list',
    //     name: 'Xextension',
    //     message: "which Xextension you want to use?",
    //     choices: ()=>{
    //         let list = [];
    //         list = getlist(path.join(Xbooks_root, 'src', 'extensions', 'extensions.list'));
    //         list.push("None");
    //         return list;
    //     }
    // },
    // {
    //     type: 'editor',
    //     name: 'biodata',
    //     message: "Author's bio to be written on profile:",
    //     validate: function (text) {
    //         if (text.split('\n').length < 1) {
    //             return 'Must be at least a line!';
    //         }
    //         return true;
    //     },
    //     default: function(){
    //         return "this is your biodata!!"
    //     }
    // },
    // {
    //     type: 'editor',
    //     name: 'blog_description',
    //     message: "blog's description to be written on profile:",
    //     validate: function (text) {
    //         if (text.split('\n').length < 1) {
    //             return 'Must be at least a line!';
    //         }
    //         return true;
    //     },
    //     default: function(){
    //         return "this is description of this blog!!";
    //     }
    // },
];

module.exports = {

    initiate: () => {
        if(! fs.existsSync(rcfile_name)){
            ccc.note("Xbooks doesn't take these information, it stores these information to a file '.Xbooksrc' in your repo as a configuration file for Xbooks!");
            let repo_url;
            inquirer.prompt(questions).then(answers => {
                repo_url = `https://github.com/${answers["GitHub_Username"]}/${answers["gh_repo_name"]}.git`;
                fs.writeFileSync(rcfile_name, JSON.stringify(answers, null, '  '));
                ccc.success("initializing Xbooks")
            }).catch((err)=>{
                if(err) process.exit(ccc.fail(err));
            }).then(()=>{
                git.checkIsRepo((err,isrepo)=>{
                    if(err) process.exit(ccc.fail(err))
                    else{
                        if(!isrepo){
                            git.init(err=>{
                                if(err) process.exit(ccc.fail(err))
                                else{
                                    ccc.success("initializing git")
                                    git.addRemote("origin", `${repo_url}`, err=>{
                                        if(err) process.exit(ccc.fail(err))
                                        else ccc.success(`adding remote ${repo_url} as origin`)
                                    }).exec(()=>{
                                        git.raw(
                                            [
                                                "config",
                                                "http.postBuffer",
                                                "524288000"
                                            ],
                                            err=>{
                                                if(err) process.exit(ccc.fail(err))
                                                else ccc.blue("Config", "configured git http.postBuffer to 524288000 Bytes")
                                            }
                                        )
                                    })
                                }
                            })
                        }
                        else ccc.note("git was already initialized!")
                    }
                })
            }).catch(err=>process.exit(ccc.fail(err)))
        }
        else console.log("Xbooks is already initialized in this directory!");

    }
}