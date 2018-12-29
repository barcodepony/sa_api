$(document).ready(function () {
    $.getJSON("http://192.168.0.157:5000/api/shops", function (data) {

        var arrItems = [];      // THE ARRAY TO STORE JSON ITEMS.
        $.each(data, function (index, value) {
            arrItems.push(value);       // PUSH THE VALUES INSIDE THE ARRAY.
        });

        // EXTRACT VALUE FOR TABLE HEADER.
        var col = [];
        for (var i = 0; i < arrItems.length; i++) {
            for (var key in arrItems[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }

        // CREATE DYNAMIC TABLE.
        var table = document.createElement("table");
        table.id = "shops_table";


        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        var tr = table.insertRow(-1);                   // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < arrItems.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = arrItems[i][col[j]];

                switch (j) {
                    case 0:
                        tabCell.setAttribute("data-field", "s_amenity");
                        break;
                    case 1:
                        tabCell.setAttribute("data-field", "s_category");
                        break;
                    case 2:
                        tabCell.setAttribute("data-field", "s_homepage");
                        break;
                    case 3:
                        tabCell.setAttribute("data-field", "s_id");
                        break;
                    case 4:
                        tabCell.setAttribute("data-field", "s_lat");
                        break;
                    case 5:
                        tabCell.setAttribute("data-field", "s_lon");
                        break;
                    case 6:
                        tabCell.setAttribute("data-field", "s_name");
                        var cell = tr.insertCell(-1);
                        cell.innerHTML = "<input type='button' onclick='delete_shop(this)' id='delete_shop_btn' value='Delete'>";
                        break;

                }
            }
        }


        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        var divContainer = document.getElementById("main_table");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    });
});



