$(document).ready(function () {
    $("#inline_editing").click(function () {

        $("#main_table tr").editable({

            save: function (values) {

                var amenity = values['s_amenity'];
                var category = values['s_category'];
                var homepage = values['s_homepage'];
                var id = values['s_id'];
                var lat = values['s_lat'];
                var lon = values['s_lon'];
                var name = values['s_name'];

                alert(name);

                var shop = {
                    "s_amenity": amenity,
                    "s_category": category,
                    "s_homepage": homepage,
                    "s_lat": parseFloat(lat),
                    "s_lon": parseFloat(lon),
                    "s_name": name
                };


                $.ajax({
                    type: "PUT",
                    url: "http://192.168.0.157:5000/api/shops/" + id,
                    // The key needs to match your method's input parameter (case-sensitive).
                    data: JSON.stringify(shop),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function (data) {
                        alert(data);
                    },
                    failure: function (errMsg) {
                        alert(errMsg);
                    }
                });


            }

        });

    });
    $("#inline_editing").click(function () {

        $("#main_table tr").editable({

            save: function (values) {

                var amenity = values['s_amenity'];
                var category = values['s_category'];
                var homepage = values['s_homepage'];
                var id = values['s_id'];
                var lat = values['s_lat'];
                var lon = values['s_lon'];
                var name = values['s_name'];

                alert(name);

                var shop = {
                    "s_amenity": amenity,
                    "s_category": category,
                    "s_homepage": homepage,
                    "s_lat": parseFloat(lat),
                    "s_lon": parseFloat(lon),
                    "s_name": name
                };


                $.ajax({
                    type: "PUT",
                    url: "http://192.168.0.157:5000/api/shops/" + id,
                    // The key needs to match your method's input parameter (case-sensitive).
                    data: JSON.stringify(shop),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function (data) {
                        alert(data);
                    },
                    failure: function (errMsg) {
                        alert(errMsg);
                    }
                });


            }

        });

        $("#history tr").editable({

            save: function (values) {

                var category = values['f_category'];
                var id = values['f_id'];
                var label = values['f_label'];
                var name = values['f_name'];
                var poi = values['f_poi'];

                var fav = {
                    "f_category": category,
                    "f_name": name,
                    "f_label": label,
                    "f_poi": poi,
                };


                $.ajax({
                    type: "PUT",
                    url: "http://192.168.0.157:5000/api/favs/" + id,
                    // The key needs to match your method's input parameter (case-sensitive).
                    data: JSON.stringify(fav),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    success: function (data) {
                        alert(data);
                    },
                    failure: function (errMsg) {
                        alert(errMsg);
                    }
                });


            }

        });

    });
});
