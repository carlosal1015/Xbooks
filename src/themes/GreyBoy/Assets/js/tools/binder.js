// https://mybinder.org/v2/gh/XinYaanZyoy/test1341/master
// ?filepath=notebooks/stories/a2_avg_w2v.ipynb
function onBinder(){
    let binder_url = "https://mybinder.org/v2/";
    let repo = "gh/$AUTHOR$/$REPO$/master";
    let connector = "?filepath=";
    let root = "notebooks/";
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let notebook = pathpoints.join("/");
    let url = binder_url + repo + connector + root + notebook;
    window.open(url, '_blank').focus();   
}