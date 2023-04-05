"use strict";

var i = [0];
var images = [];
var time = 3000;
images[0] = "./static/images/slides/a.jpg";
images[1] = "./static/images/slides/b.jpg";
images[2] = "./static/images/slides/c.jpg";
images[3] = "./static/images/slides/d.jpg";
images[4] = "./static/images/slides/e.jpg";
images[5] = "./static/images/slides/f.jpg";
images[6] = "./static/images/slides/g.jpg";

function changeImg() {
  if (i < images.length) {
    document.slide.src = images[i];
    i++;
  } else {
    i = 0;
  }

  setTimeout("changeImg()", time);
}

window.onload = changeImg;
//# sourceMappingURL=script.dev.js.map
