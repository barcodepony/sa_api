$(document).ready(function () {
    $.getJSON('dummyJsonData/poi.json', function(data){
        $.each(data, function (i, value) {
           $('<option>' + value +"("+  i  +")" + '</option>').appendTo('#poi');
        });
    });
});