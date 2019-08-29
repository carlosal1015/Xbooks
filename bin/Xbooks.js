#!/usr/bin/env node

'use strict';

const pkg = require('../package');
const ccc = require("../lib/common_cli_conventions");
const initiator = require('../lib/initiator');
const installer = require("../lib/installer/install");
const placifier  = require("../lib/placifier/placify");
const publisher = require("../lib/publisher/publish");
const syncer = require("../lib/publisher/syncer");
const uninstaller = require("../lib/uninstaller/uninstall");

const cmd = require('commander');
const path = require('path');

const {getInstalledPathSync} = require('get-installed-path');
const Xbooks_PATH = getInstalledPathSync('@xsoft/xbooks');

ccc.greet("hola! lots of hopes and wishes for your project! from the writter of Xbooks; XinYaanZyoy! \
       \nhttps://GitHub.com/XinYaanZyoy")
ccc.alert(ccc.logo("Xbooks" + pkg.version)+" is under development process!!");

const updateNotifier = require('update-notifier');
updateNotifier({pkg}).notify();

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
        installer.install(Xbooks_PATH, path.resolve());
    })

cmd
   .command("placify")
   .alias('p')
   .description("to placify your blog according to .Xbooksrc")
   .action(()=>{
       placifier.placify();
   })

cmd
   .command("publish")
   .alias('pub')
   .description("to publish your blog to GitHub-Pages")
   .option("-i, --initial", "to pubish for the first time")
   .action((cmd)=>{
       publisher.publish(cmd.initial);
   })

cmd
   .command("synchronize")
   .alias("sync")
   .description("to sync with the remote if needed (though before every commit it's done)")
   .action(()=>{
       syncer.sync();
   })

cmd
    .command("uninstall")
    .alias('uni')
    .description("to uninstall all Xbooks and all those Xbooks releated and created by Xbooks files!")
    .option('-f, --full', "to fully uninstall Xbooks")
    .action((cmd)=>{
        uninstaller.uninstall(cmd.full);
    })

// cmd
//     .command("serve")
//     .alias("s")
//     .description("serve your blog on port:1969||xxxx")
//     .action(()=>{
//         server.serve();
//     })

cmd
    .version(pkg.version, '-v, --version')

cmd
    .on('--help', ()=>{
    console.log('')
    console.log('Example:');
    ccc.code(["npm i -g @xsoft/xbooks",
              "mkdir example_blog && chdir example_blog",
              "Xbooks init",
              "Xbooks placify",
              "Xbooks install",
              "Xbooks pub -i"
            ]);
  });

if(!process.argv.slice(2).length) cmd.help();
cmd.parse(process.argv)