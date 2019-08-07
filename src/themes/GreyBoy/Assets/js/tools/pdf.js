function toPDF() {
    const gh_url = 'https://github.com/';

    let repo = "$GH$/$REPO$/"
    let connector = "raw/"
    let root = "master/docs/pdfs/"
    let pathpoints = Object.entries(document.getElementsByClassName('virtual'));
    let pointnames = []
    for(let ele of pathpoints){
        pointnames.push(ele[1].innerText);
    }
    let notebook = pointnames.join("/");
    let url = gh_url + repo + connector + root + notebook + '.pdf';
    window.open(url, '_blank').focus();
}