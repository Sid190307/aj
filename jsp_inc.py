
<%@ page contentType="text/html" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Include JSP Pages</title>
</head>
<body>

    <font color="red">
        Include the First File:
    </font>

    <br><br>

    <jsp:include page="p1.jsp" />

    <br><br><br>

    <font color="blue">
        Include the Second File:
    </font>

    <br><br>

    <jsp:include page="orderform.jsp" />

</body>
</html>
