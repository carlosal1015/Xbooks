function onGitPod(){
    let gitpod_url = "https://gitpod.io/";
    let connector = "#https://";
    let repo = "github.com/$AUTHOR$/$REPO$/";
    let root = "blob/master/notebooks/";
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let notebook = pathpoints.join("/");
    let url = gitpod_url + connector + repo + root + notebook + '.ipynb';
    window.open(url, '_blank').focus();
}