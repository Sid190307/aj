
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Fibonacci Series</title>
</head>
<body>

    <h1>Fibonacci Series</h1>

    <form action="p2.jsp" method="get">

        <label for="val">Enter a value for n:</label>
        <input type="number" id="val" name="val"
               min="0" max="30" required>

        <br><br>

        <input type="submit" value="Submit">

    </form>

</body>
</html>


<%@ page contentType="text/html" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Fibonacci Series</title>
</head>
<body>

    <h1>Fibonacci Series</h1>

    <%!
        int fibo(int n) {
            if (n < 2)
                return n;
            else
                return fibo(n - 1) + fibo(n - 2);
        }
    %>

    <%
        String str = request.getParameter("val");

        if (str == null || str.trim().isEmpty()) {
            out.println("Please enter a value for n.");

        } else {
            try {
                int n = Integer.parseInt(str);

                if (n < 0 || n > 30) {
                    out.println("Please enter n between 0 and 30.");

                } else {
                    out.println("<b>Fibonacci series up to "
                            + n + ":</b><br><br>");

                    for (int i = 0; i <= n; i++) {
                        out.print(fibo(i) + " ");
                    }
                }

            } catch (NumberFormatException e) {
                out.println("Invalid input. Please enter an integer.");
            }
        }
    %>

</body>
</html>
