
<!DOCTYPE html>
<html>
<head>
    <title>Creation of Array Object in JavaScript Using JSON</title>
</head>
<body>

    <script>
        document.writeln("<h2>JSON Array Object</h2>");

        var books = {
            "Pascal": [
                {
                    "Name": "Pascal Made Simple",
                    "price": 700
                },
                {
                    "Name": "Guide to Pascal",
                    "price": 400
                }
            ],

            "Scala": [
                {
                    "Name": "Scala for the Impatient",
                    "price": 1000
                },
                {
                    "Name": "Scala in Depth",
                    "price": 1300
                }
            ]
        };

        var i;

        document.writeln("<table border='2'><tr>");

        // Display Pascal books
        for (i = 0; i < books.Pascal.length; i++) {
            document.writeln("<td>");
            document.writeln("<table border='1' width='200'>");

            document.writeln(
                "<tr><td><b>Name</b></td><td>" +
                books.Pascal[i].Name + "</td></tr>"
            );

            document.writeln(
                "<tr><td><b>Price</b></td><td>" +
                books.Pascal[i].price + "</td></tr>"
            );

            document.writeln("</table>");
            document.writeln("</td>");
        }

        // Display Scala books
        for (i = 0; i < books.Scala.length; i++) {
            document.writeln("<td>");
            document.writeln("<table border='1' width='200'>");

            document.writeln(
                "<tr><td><b>Name</b></td><td>" +
                books.Scala[i].Name + "</td></tr>"
            );

            document.writeln(
                "<tr><td><b>Price</b></td><td>" +
                books.Scala[i].price + "</td></tr>"
            );

            document.writeln("</table>");
            document.writeln("</td>");
        }

        document.writeln("</tr></table>");
    </script>

</body>
</html>
