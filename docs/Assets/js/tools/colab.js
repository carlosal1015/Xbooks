// https://raw.githubusercontent.com/googlecolab/open_in_colab/master/js/background.js

/*
    Copyright 2018 Google LLC

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
*/

// This listener is called when the user clicks the extension icon.

// If the current URL matches a Jupyter notebook hosted on github.com
// or on gist.github.com, this function will open a new tab and load
// the notebook into Colab.

// edited by XinYaanZyoy (https://github.com/XinYaanZyoy)

function onColab() {
    const colab_url = 'https://colab.research.google.com/';

    let repo = "github/xsoft-technologies/Xbooks/"
    let root = "blob/master/notebooks/"
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let pointnames = []
    for(let ele of pathpoints){
        pointnames.push(ele[1].innerText);
    }
    let notebook = pointnames.join("/");
    let url = colab_url + repo + root + notebook + '.ipynb';
    window.open(url, '_blank').focus();
}