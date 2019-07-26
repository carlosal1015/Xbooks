#!/usr/bin/env node

'use strict';

const inquirer = require('inquirer');
const fs = require('fs');
const path = require('path');

const ccc = require('../lib/common_cli_conventions');

const rcfile_name = ".Xbooksrc";
const Xbooks_root = path.join(process.argv[1].replace(path.join("bin","Xbooks.js"), ""));

inquirer.registerPrompt('directory', require('inquirer-select-directory'));

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
    return fs.readFileSync(filepath).toString().split('\n');
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
    {
        type: 'input',
        name: 'phone',
        message: "What's your phone number",
        validate: function (value) {
            var pass = value.match(
                /^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$/i
            );
            if (pass || value=="") {
                return true;
            }

            return 'Please enter a valid phone number';
        }
    },
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
    {
        type: 'list',
        name: 'Xplugin',
        message: "which Xplugin you want to use?",
        choices: ()=>{
            let list = [];
            list = getlist(path.join(Xbooks_root, 'src', 'plugins', 'plugins.list'));
            list.push("None");
            return list;
        }
    },
    {
        type: 'list',
        name: 'Xextension',
        message: "which Xextension you want to use?",
        choices: ()=>{
            let list = [];
            list = getlist(path.join(Xbooks_root, 'src', 'extensions', 'extensions.list'));
            list.push("None");
            return list;
        }
    },
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
    {
        type: 'directory',
        name: 'JNbooks',
        message: "choose directory of your jupyter notebooks:",
        basePath: '.',
        default: function () {
            return 'notebooks';
        }
    },
    {
            type: 'directory',
            name: 'Xbooks',
            message: "choose directory of Xbooks generated files[GitHub uses docs/ for hosting github pages]:",
            basePath: '.',
            default: function () {
            return 'docs';
        }
    }
];

module.exports = {

    initiate: () => {
        if(! fs.existsSync(rcfile_name)){
            ccc.note("Xbooks doesn't take these information, it stores these information to a file '.Xbooksrc' in your repo as a configuration file for Xbooks!");

            inquirer.prompt(questions).then(answers => {
                answers["JNbooks"] = path.join('.', path.basename(answers["JNbooks"]), '/');
                answers['Xbooks'] = path.join('.', path.basename(answers['Xbooks']), '/');
                fs.writeFileSync(rcfile_name, JSON.stringify(answers, null, '  '));
            }).catch((err)=>{
                if(err){
                    process.exit(ccc.fail(err));
                }
                else ccc.success("writing .Xbooksrc")
            })
        }
        else console.log("Xbooks is already initialized in this directory!");

    }
}