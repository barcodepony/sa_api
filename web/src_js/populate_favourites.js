$(document).ready(function () {
    $.getJSON("http://192.168.0.157:5000/api/favs", function (data) {

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
        table.id = "favs_table";

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
                        tabCell.setAttribute("data-field", "f_category");
                        break;
                    case 1:
                        tabCell.setAttribute("data-field", "f_id");
                        break;
                    case 2:
                        tabCell.setAttribute("data-field", "f_label");
                        break;
                    case 3:
                        tabCell.setAttribute("data-field", "f_name");
                        break;
                    case 4:
                        tabCell.setAttribute("data-field", "f_poi");
                        break;
            }}
        }

        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        var divContainer = document.getElementById("history");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    });
});



