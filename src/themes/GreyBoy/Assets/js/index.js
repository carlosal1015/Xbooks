function fscreen(){
    if (document.fullscreenEnabled ||
        document.webkitFullscreenEnabled ||
        document.mozFullScreenEnabled ||
        document.msFullscreenEnabled) {

        let Xdisplay = document.getElementById('Xdisplay');

        if (Xdisplay.requestFullscreen) {
            Xdisplay.requestFullscreen();
        } else if (Xdisplay.webkitRequestFullscreen) {
            Xdisplay.webkitRequestFullscreen();
        } else if (Xdisplay.mozRequestFullScreen) {
            Xdisplay.mozRequestFullScreen();
        } else if (Xdisplay.msRequestFullscreen) {
            Xdisplay.msRequestFullscreen();
        }

        Xdisplay.src = Xdisplay.src;
    }
    else console.log("unsupported browser!")
}

function updateExplorer(des) {

    document.getElementById('loadImg').style.display = 'block';
    document.getElementById('Xdisplay').style.display = 'none';

    let explorer = document.getElementById("explorer");
    let virtual = document.getElementsByClassName("virtual");

    while (virtual[0]) {
        virtual[0].parentNode.removeChild(virtual[0]);
    }
    par = "notebooks/";
    des.split("/").forEach((ele) => {
        if (ele != "notebooks" && ele != "welcome.html" && ele != "index.html") {
            let node = document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item virtual");
            node.style.cursor = "pointer";
            let a = document.createElement("A");
            if (!ele.includes(".html")) {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}/index.html"); updateExplorer("${par}/${ele}/index.html")`);
                par = `${par}/${ele}`
            } else {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}"); updateExplorer("${par}/${ele}")`);
                par = `${par}/${ele.replace(".html", "")}`
            }
            let textnode = document.createTextNode(ele.replace(".html", ""));
            a.appendChild(textnode);
            node.appendChild(a);
            explorer.appendChild(node);
        }
    })
}


function updateExplorer_IFrame(des) {

    window.parent.document.getElementById('loadImg').style.display = 'block';
    window.parent.document.getElementById('Xdisplay').style.display = 'none';

    let explorer = window.parent.document.getElementById("explorer");
    let virtual = window.parent.document.getElementsByClassName("virtual");

    while (virtual[0]) {
        virtual[0].parentNode.removeChild(virtual[0]);
    }
    par = "notebooks/";
    des.split("/").forEach((ele) => {
        if (ele != "notebooks" && ele != "welcome.html" && ele != "index.html") {
            let node = window.parent.document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item virtual");
            node.style.cursor = "pointer";
            let a = window.parent.document.createElement("A");
            if (!ele.includes(".html")) {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}/index.html"); updateExplorer("${par}/${ele}/index.html")`);
                par = `${par}/${ele}`
            } else {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}"); updateExplorer("${par}/${ele}")`);
                par = `${par}/${ele.replace(".html", "")}`
            }
            let textnode = window.parent.document.createTextNode(ele.replace(".html", ""));
            a.appendChild(textnode);
            node.appendChild(a);
            explorer.appendChild(node);
        }
    });
}