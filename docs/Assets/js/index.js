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
        if (ele != "notebooks" && ele != "welcome.html" && ele != "index.html" && ele != "\\Xbooks" && ele != "") {
            let node = document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item virtual");
            node.style.cursor = "pointer";
            let a = document.createElement("A");
            if (!ele.includes(".html")) {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}/index.html"); updateExplorer("${par}/${ele}/index.html")`);
                par = `${par}/${ele}`

                let obj = Array(document.getElementsByClassName("tools"))[0]
                for (let key of Object.keys(obj)){
                    obj[key].style.display = "none";
                }

            } else {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}"); updateExplorer("${par}/${ele}")`);
                par = `${par}/${ele.replace(".html", "")}`

                let obj = Array(document.getElementsByClassName("tools"))[0]
                for (let key of Object.keys(obj)){
                    obj[key].style.display = "";
                }

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
        if (ele != "notebooks" && ele != "welcome.html" && ele != "index.html" && ele != "\\Xbooks" && ele != "") {
            let node = window.parent.document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item virtual");
            node.style.cursor = "pointer";
            let a = window.parent.document.createElement("A");
            if (!ele.includes(".html")) {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}/index.html"); updateExplorer("${par}/${ele}/index.html")`);
                par = `${par}/${ele}`

                let obj = Array(window.parent.document.getElementsByClassName("tools"))[0]
                for (let key of Object.keys(obj)){
                    obj[key].style.display = "none";
                }

            } else {
                a.setAttribute("onclick", `document.getElementById('Xdisplay').contentWindow.location.replace("${par}/${ele}"); updateExplorer("${par}/${ele}")`);
                par = `${par}/${ele.replace(".html", "")}`

                let obj = Array(window.parent.document.getElementsByClassName("tools"))[0]
                for (let key of Object.keys(obj)){
                    obj[key].style.display = "";
                }

            }
            let textnode = window.parent.document.createTextNode(ele.replace(".html", ""));
            a.appendChild(textnode);
            node.appendChild(a);
            explorer.appendChild(node);
        }
    });
}