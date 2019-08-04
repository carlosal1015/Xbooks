function onGitPod(){
    let gitpod_url = "https://gitpod.io/";
    let connector = "#https://";
    let repo = "github.com/$GH$/$REPO$/";
    let root = "blob/master/notebooks/";
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let pointnames = [];
    for(let ele of pathpoints){
        pointnames.push(ele[1].innerText);
    }
    let notebook = pointnames.join("/");
    let url = gitpod_url + connector + repo + root + notebook + '.ipynb';
    window.open(url, '_blank').focus();
}