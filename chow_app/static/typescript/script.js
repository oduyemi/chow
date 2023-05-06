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
    }
    else {
        i = 0;
    }
    setTimeout("changeImg()", time);
}
window.onload = changeImg;


$(document).ready(function () {
    $("#livebox").on("input", function (e) {
        var live_text = $(this).val();
        $.ajax({
            method: "POST",
            url: "/livesearch",
            data: { text: live_text },
            success: function (rsp) {
                var data = "<ul>";
                $.each(rsp, function (index, value) {
                    data += "<li style='list-style:none'>" + value.menu_item + "<li>";
                });
                data += "</ul>";
                $("#menulist").html(data);
            }
        });
    });
    $("#menu_item").on("input", function (e) {
        var live_text2 = $(this).val();
        $.ajax({
            method: "POST",
            url: "/livesearch2",
            data: { text: live_text2 },
            success: function (res) {
                var data = "<ul>";
                $.each(res, function (index, value) {
                    data += "<li style='list-style:none'>" + value.menu_item + "<li>";
                });
                data += "</ul>";
                $("#fooditem").html(data);
            }
        });
    });
});


$('.add-to-cart').click(function() {
    var itemId = $(this).data('item-id');
    var itemPrice = $(this).data('item-price');
  
    // Add the item to the cart object in your Flask app.
    app.cart[itemId] = {
      price: itemPrice
    };
  
    // Update the cart icon in the navigation menu to show the number
    // of items in the cart.
    updateCartIcon();
  });

  function updateCartIcon() {
    var numItems = Object.keys(app.cart).length;
    $('.cart-icon').text(numItems);
  }

  
$('#checkout').click(function() {
    // Convert the cart object to a JSON string.
    var cartData = JSON.stringify(app.cart);
  
    // Send the cart data to your server using AJAX.
    $.ajax({
      type: 'POST',
      url: '/checkout',
      data: cartData,
      contentType: 'application/json',
      success: function(response) {
        // Handle the server response.
      },
      error: function(xhr) {
        // Handle the error.
      }
    });
  });

  function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }


var geocoder = new google.maps.Geocoder();

function geocodeAddress(address) {
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === 'OK') {
      var location = results[0].geometry.location;
      var lat = location.lat();
      var lng = location.lng();
      // Do something with the latitude and longitude coordinates
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}
