#!/usr/bin/env node

'use strict';

const ccc = require("../common_cli_conventions");
const git = require("simple-git")(require("path").resolve());
const fs = require("fs");

git.silent(true);

module.exports = {
    sync: () => {
        fs.readFile(".Xbooksrc", (err, data) => {
            if (err) process.exit(ccc.fail(err))
            else {
                data = JSON.parse(data);
                ccc.success("reading Xbooksrc");
                git.pull(`https://github.com/${data["GitHub_Username"]}/${data["gh_repo_name"]}.git`, "master", (err,ups) => {
                    if (err) process.exit(ccc.fail(err));
                    else{
                        ccc.success(`pulling from remote https://github.com/${data["Github_Username"]}/${data["gh_repo_name"]}.git master`);
                        ccc.blue("Updates", JSON.stringify(ups, null, "  "));
                    }
                });
            }
        })
    }
}