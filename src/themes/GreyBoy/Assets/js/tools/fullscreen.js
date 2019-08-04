function fscreen() {
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

        Xdisplay.src = Xdisplay.contentWindow.location.href;
    } else console.log("unsupported browser!")
}