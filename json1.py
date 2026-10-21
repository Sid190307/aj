
<!DOCTYPE html>
<html>
<head>
    <title>JSON Example</title>
</head>
<body>

    <script>
        var object1 = {
            "language": "Java",
            "author": "Herbert Schildt"
        };

        document.write("<h1>JSON with JavaScript Example</h1>");
        document.write("<br>");

        document.write("<h3>Language = " + object1.language + "</h3>");
        document.write("<h3>Author = " + object1.author + "</h3>");

        var object2 = {
            "language": "C++",
            "author": "E-Balagurusamy"
        };

        document.write("<br>");

        document.write("<h3>Language = " + object2.language + "</h3>");
        document.write("<h3>Author = " + object2.author + "</h3>");

        document.write("<hr>");

        document.write(
            object2.language +
            " programming language can be studied from book written by " +
            object2.author
        );

        document.write("<hr>");
    </script>

</body>
</html>
