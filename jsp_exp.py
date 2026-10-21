
<%@ page contentType="text/html" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Power of 2</title>
</head>
<body>

    <center>
        <h1>Powers of 2</h1>
    </center>

    <table border="2" align="center">
        <tr>
            <th>Exponent</th>
            <th>2^Exponent</th>
        </tr>

        <% for (int i = 0; i <= 10; i++) { %>
        <tr>
            <td><%= i %></td>
            <td><%= (int) Math.pow(2, i) %></td>
        </tr>
        <% } %>
    </table>

</body>
</html>
