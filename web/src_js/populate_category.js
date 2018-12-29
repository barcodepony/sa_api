$(document).ready(function () {
    $.getJSON("http://192.168.0.157:5000/api/shops/category", function(data){
        $.each(data, function (i, value) {
           $('<option>' + value + '</option>').appendTo('#category');
        });
    });
});