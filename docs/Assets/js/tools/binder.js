// https://mybinder.org/v2/gh/XinYaanZyoy/test1341/master
// ?filepath=notebooks/stories/a2_avg_w2v.ipynb
function onBinder(){
    let binder_url = "https://mybinder.org/v2/";
    let repo = "gh/xsoft-technologies/Xbooks/master";
    let connector = "?filepath=";
    let root = "notebooks/";
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let pointnames = []
    for(let ele of pathpoints){
        pointnames.push(ele[1].innerText);
    }
    let notebook = pointnames.join("/") + '.ipynb';
    let url = binder_url + repo + connector + root + notebook;
    window.open(url, '_blank').focus();   
}