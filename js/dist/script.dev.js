"use strict";

var i = [0];
var images = [];
var time = 3000;
images[0] = "./images/slides/a.jpg";
images[1] = "./images/slides/b.jpg";
images[2] = "./images/slides/c.jpg";
images[3] = "./images/slides/d.jpg";
images[4] = "./images/slides/e.jpg";
images[5] = "./images/slides/f.jpg";
images[6] = "./images/slides/g.jpg";

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
