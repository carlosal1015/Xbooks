#!/usr/bin/env node

'use strict';

const colors = require('colors');
const box = require("boxen");

module.exports = {

    success: (txt)=>{
        console.log(colors.bgGreen("|Success|")+colors.green('> '+txt));
    },

    fail: (txt)=>{
        console.log(colors.bgRed("|Failure|")+colors.red('> '+txt));
    },

    alert: (txt)=>{
        console.log(colors.bgYellow("|Alert|")+colors.yellow('> '+txt));
    },

    note: (txt)=>{
        console.log(colors.bgCyan("|Note|")+colors.cyan('> '+txt));
    },

    greet: (txt)=>{
        console.log(colors.bgMagenta("|Greetings|")+colors.magenta('> '+txt));
    },

    logo: (txt)=>{
        return colors.bgWhite.black.dim('|'+txt+'|');
    },

    blue: (tag, txt)=>{
        console.log(colors.bgBlue("|"+tag+"|")+colors.blue("> "+txt).bold);
    },

    green: (tag, txt)=>{
        console.log(colors.bgGreen('|'+tag+'|')+colors.green("> "+txt));
    },

    yellow: (tag, txt)=>{
        console.log(colors.bgYellow('|'+tag+'|')+colors.yellow("> "+txt));
    },

    red: (tag, txt)=>{
        console.log(colors.bgRed('|'+tag+'|')+colors.red("> "+txt));
    },

    cyan: (tag, txt)=>{
        console.log(colors.bgCyan('|'+tag+'|')+colors.cyan("> "+txt));
    },

    magenta: (tag, txt)=>{
        console.log(colors.bgMagenta('|'+tag+'|')+colors.magenta("> "+txt));
    },

    code: (script, list)=>{
        let scriptbox = ""
        if(list)
            var i = 1
        script.forEach(codeline => {
            if(list){
                scriptbox += i+". ".black+codeline.white+'\n';
                i=i+1;    
            }
            else
                scriptbox += "$ ".black+codeline.white+'\n';
        });
        console.log(box(scriptbox, {margin: 1, padding: 1, borderStyle: "round", borderColor: "green", float: "left", backgroundColor: "#888"}));
    }
}