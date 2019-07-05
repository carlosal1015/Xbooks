#!/usr/bin/env node

'use strict';

const pkg = require('../package');
const initiator = require('../lib/initiator');
const ccc = require("../lib/ccc/common_cli_conventions");
const installer = require("../lib/installer/initiator");
const server = require("../lib/server/server");

const cmd = require('commander');
const path = require('path');

ccc.alert("Xbooks is under development process!!");

cmd
    .command('initialize')
    .alias('init')
    .description("initialize an Xbooks project in CWD!")
    .action(()=>{
        initiator.initiate();
    });

cmd
    .command("install")
    .alias('i')
    .description("to install dependencies defined in .Xbooksrc")
    .action(()=>{
        installer.install(process.argv[1].replace(path.join("bin","Xbooks.js"), ""), path.resolve());
    })

cmd
    .command("serve")
    .alias("s")
    .description("serve your blog on port:1969||xxxx")
    .action(()=>{
        server.serve();
    })

cmd
    .command("convert")
    .description("convert your ipynbs to html")

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