{/* <li style="cursor: pointer" class="breadcrumb-item">
                <a style="--link-color:rgb(100, 172, 232) !important; --link-color-hover:rgb(126, 187, 236) !important;
                --link-color-active:rgb(100, 172, 232) !important; --visited-color:rgb(148, 100, 232) !important;
                --visited-color-hover:rgb(167, 126, 236) !important; --visited-color-active:rgb(148, 100, 232)
                !important;" onclick="document.getElementById('Xdisplay').contentWindow.location.replace('notebooks/nb001/b01.html')">b01</a>
            </li> */}

function updateExplorer(des){
    let explorer = document.getElementById("explorer");
    let virtual = document.getElementsByClassName("virtual");

    while(virtual[0]) {
        virtual[0].parentNode.removeChild(virtual[0]);
    }
    par = "notebooks/";
    des.split("/").forEach((ele)=>{
        if(ele != "notebooks" && ele != "welcome.html" && ele != "index.html"){
            let node = document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item");
            node.setAttribute("class", "virtual");
            node.style.cursor = "pointer";
            let a = document.createElement("A");
            if(!ele.includes(".html")){
                a.setAttribute("onclick", "document.getElementById('Xdisplay').contentWindow.location.replace('" + '/'+par+ele+'/'+"index.html" + "'); updateExplorer('" + par+ele+'/'+'index.html' + "')");
                par = par + ele + '/'
            }
            else{
                a.setAttribute("onclick", "document.getElementById('Xdisplay').contentWindow.location.replace('" + '/'+par+ele + "'); updateExplorer('" + par+ele + "')");
                par = par + ele.replace(".html", "") + '/'
            }
            let textnode = document.createTextNode(ele.replace(".html", ""));
            a.appendChild(textnode);
            node.appendChild(a);
            explorer.appendChild(node);
        }
    })
}


function updateExplorer_IFrame(des){
    let explorer = window.parent.document.getElementById("explorer");
    let virtual = window.parent.document.getElementsByClassName("virtual");

    while(virtual[0]) {
        virtual[0].parentNode.removeChild(virtual[0]);
    }
    par = "notebooks/";
    des.split("/").forEach((ele)=>{
        if(ele != "notebooks" && ele != "welcome.html" && ele != "index.html"){
            let node = window.parent.document.createElement("LI");
            node.setAttribute("class", "breadcrumb-item");
            node.setAttribute("class", "virtual");
            node.style.cursor = "pointer";
            let a = window.parent.document.createElement("A");
            if(!ele.includes(".html")){
                a.setAttribute("onclick", "document.getElementById('Xdisplay').contentWindow.location.replace('" + '/'+par+ele+'/'+"index.html" + "'); updateExplorer('" + par+ele+'/'+'index.html' + "')");
                par = par + ele + '/'
            }
            else{
                a.setAttribute("onclick", "document.getElementById('Xdisplay').contentWindow.location.replace('" + '/'+par+ele + "'); updateExplorer('" + par+ele + "')");
                par = par + ele.replace(".html", "") + '/'
            }
            let textnode = window.parent.document.createTextNode(ele.replace(".html", ""));
            a.appendChild(textnode);
            node.appendChild(a);
            explorer.appendChild(node);
        }
    });
}