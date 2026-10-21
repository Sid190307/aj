
<%@ page contentType="text/html" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Order Form</title>
</head>
<body>

    <center>
        <h1>Order Form</h1>
    </center>

    <%!
        String item[] = {"DVD", "CD", "Diskette"};
        double price[] = {19.9, 12.88, 1.88};
        int quantity[] = {2, 9, 4};
    %>

    <table align="center" bgcolor="lightgrey"
           border="1" width="75%">

        <tr>
            <th>Item</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total Price</th>
        </tr>

        <% for (int i = 0; i < item.length; i++) { %>
        <tr>
            <td><%= item[i] %></td>
            <td><%= price[i] %></td>
            <td><%= quantity[i] %></td>
            <td><%= price[i] * quantity[i] %></td>
        </tr>
        <% } %>

    </table>

</body>
</html>
