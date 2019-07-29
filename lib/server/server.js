#!/usr/bin/env node

'use strict';

const fs = require("fs");
const path = require("path");
const ccc = require("../common_cli_conventions");

var bs = require("browser-sync").create();

module.exports = {
    serve: ()=>{
        if(fs.existsSync(path.join(".", "docs", "index.html"))){
            bs.init({
                server: "./docs",
                watch: true,
                    ui: {
                        port: 1905
                    },
                    port: 1969,
                    notify: true
                });

                bs.reload("*.*");

                bs.emitter.on("init", function () {
                    console.log("Xbooks uses browsersync to serve your blog offline to your machine and its network!",
                    "\nsince Xbooks is meant for pipelined or automated blog this serving on local machine is redundant"
                    ,"\nbut if you still want to inspect output of your newly created jupyter notebooks",
                    "\nkindly consider to convert your jupyter notebooks before serving!(this'll skip(though it'll run but won't push anything) the pipeline script on this commit to github)",
                    "\n\tby running $ Xbooks c [convert]");
                });
        }
        else{
            console.log("Xbooks is not installed properly!\nkindly, run\n");
            ccc.code(["xbooks install"]);
        }
    }
}