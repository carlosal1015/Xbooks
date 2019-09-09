#!/usr/bin/env node

'use strict';

const pkg = require('../package');
const ccc = require("../lib/common_cli_conventions");
const initiator = require('../lib/initiator');
const installer = require("../lib/installer");
const placifier = require("../lib/placifier");
const publisher = require("../lib/publisher");
const syncer = require("../lib/syncer");
const uninstaller = require("../lib/uninstaller");

const cmd = require('commander');
const path = require('path');
const fs = require("fs");

const {
    getInstalledPathSync
} = require('get-installed-path');
const Xbooks_PATH = getInstalledPathSync('@xsoft/xbooks');

ccc.greet("hola! lots of hopes and wishes for your project! from the writter of Xbooks; XinYaanZyoy! \
       \nhttps://GitHub.com/XinYaanZyoy")
ccc.alert(ccc.logo("Xbooks" + pkg.version) + " is under development process!!");

const updateNotifier = require('update-notifier');
const notifier = updateNotifier({
    pkg,
    updateCheckInterval: 1000 * 60 * 60 * 24
}); //every day

if (notifier.update) {
    ccc.code([
        "update " + notifier.update.name,
        "from v" + notifier.update.current + " to " + notifier.update.latest,
        "by running ",
        "npm i -g @xsoft/xbooks",
        "updtaes: " + notifier.update.type
    ]);
}

cmd
    .command('initialize')
    .alias('init')
    .description("initialize an Xbooks project in CWD!")
    .action(() => {
        initiator.initiate();
    });

cmd
    .command("install")
    .alias('i')
    .description("to install dependencies defined in .Xbooksrc")
    .action(() => {
        installer.install(Xbooks_PATH, path.resolve());
    })

cmd
    .command("placify")
    .alias('p')
    .description("to placify your blog according to .Xbooksrc")
    .action(() => {
        placifier.placify();
    })

const getlist = (filepath) => {
    if (fs.existsSync(filepath))
        return fs.readFileSync(filepath).toString().split('\n');
    else
        return []
}

cmd
    .command("list")
    .alias("l")
    .description("list of specified thing")
    .option("--themes", "list of available Xthemes")
    .option("--ci", "list of available CI script templates")
    .option("--plugins", "list of available Xplugins")
    .option("--extensions", "list of available extensions")
    .action((cmd) => {
        if (cmd.themes)
            ccc.code(getlist(path.join(Xbooks_PATH, 'src', 'themes', 'themes.list')), true)
        if (cmd.ci)
            ccc.code(getlist(path.join(Xbooks_PATH, 'src', 'CI', 'CI.list')), true)
        if (cmd.plugins)
            ccc.code(getlist(path.join(Xbooks_PATH, 'src', 'plugins', 'plugins.list')), true)
        if (cmd.extensions)
            ccc.code(getlist(path.join(Xbooks_PATH, 'src', 'extensions', 'extensions.list')), true)
    })

cmd
    .command("publish")
    .alias('pub')
    .description("to publish your blog to GitHub-Pages")
    .option("-i, --initial", "to pubish for the first time")
    .action((cmd) => {
        publisher.publish(cmd.initial);
    })

cmd
    .command("synchronize")
    .alias("sync")
    .description("to sync with the remote if needed (though before every commit it's done)")
    .action(() => {
        syncer.sync();
    })

cmd
    .command("uninstall")
    .alias('uni')
    .description("to uninstall all Xbooks and all those Xbooks releated and created by Xbooks files!")
    .option('-f, --full', "to fully uninstall Xbooks")
    .action((cmd) => {
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
    .on('--help', () => {
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

cmd
    .on("command:*", () => {
        ccc.fail('Invalid command: %s\nSee --help for a list of available commands.', cmd.args.join(' '));
        process.exit(1);
    })


if (!process.argv.slice(2).length) cmd.help();
cmd.parse(process.argv)