#!/usr/bin/env node

'use strict';

const pkg = require('../package.json');
const initiator = require('../lib/initiator.js');
const ccc = require("../lib/common_cli_conventions.js");

const cmd = require('commander');
const path = require('path');

const Xbooks_root = path.join(process.argv[1].replace('\\xbooks\\bin\\Xbooks.js', '\\xbooks'));

ccc.alert("Xbooks is under development process!!");

cmd
    .command('initialize')
    .alias('init')
    .description("initialize an Xbooks project in CWD!")
    .action(()=>{
        initiator.initiate();
    });

cmd
    .version(pkg.version, '-v, --version')

cmd
    .on('--help', ()=>{
    console.log('')
    console.log('Example:');
    ccc.code(["npm i -g @xsoft/xbooks  (if weak internet connection)",
              "npx @xsoft/xbooks  (if strong internet connection)",
              "mkdir example_blog && chdir example_blog",
              "Xbooks init  (to configure example_blog)",
              "Xbooks install  (to install configured dependencies)",
              "Xbooks convert  (to convert ipynbs to webpages)",
              "Xbooks serve  (to have a look at your blog)",
              "Xbooks edit  (to reconfigure example_blog)",
              "git add && commit && push  (to publish example_blog)",
            ]);
  });

if((!process.argv.slice(2).length)){
    ccc.note("Xbooks " + pkg.version + " is a cli based cloud pipelined software\r\nto produce a website out of a repo of jupyter notebooks on GitHub.com repo hosting service! " + "\nas of now Git-GitHub-GitLab is prefrenced! but there's more to work on!\n");
    cmd.help();
}

cmd.parse(process.argv)