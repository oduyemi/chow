let i: any =[0];
let images: any = []
let time: number = 3000;

images [0]="./static/images/slides/a.jpg"
images [1]="./static/images/slides/b.jpg"
images [2]="./static/images/slides/c.jpg"
images [3]="./static/images/slides/d.jpg"
images [4]="./static/images/slides/e.jpg"
images [5]="./static/images/slides/f.jpg"
images [6]="./static/images/slides/g.jpg"


function changeImg(){
  let silde;
    if(i<images.length){
        document.slide.src= images[i]
        i ++
    }else{i = 0}
setTimeout("changeImg()", time);
}
window.onload=changeImg;

$(document).ready(function(){
    $("#livebox").on("input", function(e){
        var live_text = $(this).val();
        
        $.ajax({
          method:"POST",
          url:"/livesearch",
          data:{text:live_text},
          success:function(rsp){
            var data = "<ul>";
              $.each(rsp, function(index, value){
                data += "<li style='list-style:none'>"+value.menu_item+"<li>"
              })
              data += "</ul>";
              $("#menulist").html(data);
          }
  
        })
  
      });

      $("#menu_item").on("input", function(e){
        var live_text2 = $(this).val();
        
        $.ajax({
          method:"POST",
          url:"/livesearch2",
          data:{text:live_text2},
          success:function(res){
            var data = "<ul>";
              $.each(res, function(index, value){
                data += "<li style='list-style:none'>"+value.menu_item+"<li>"
              })
              data += "</ul>";
              $("#fooditem").html(data);
          }
  
        })
  
      });
  
})


