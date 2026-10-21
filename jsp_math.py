
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Enter a Number</title>
</head>
<body>

    <h1>Number Form</h1>

    <form action="p2.jsp" method="get">

        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>

        <br><br>

        <button type="submit">Submit</button>

    </form>

</body>
</html>


<%@ page contentType="text/html" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Math Operations</title>
</head>
<body>

    <h1>Mathematical Operations</h1>

    <%
        String input = request.getParameter("number");

        if (input == null || input.trim().isEmpty()) {
            out.println("Please enter a number.");

        } else {
            try {
                int num = Integer.parseInt(input);

                if (num < 0) {
                    out.println("Please enter a non-negative number.");

                } else {
                    // Check even or odd
                    if (num % 2 == 0) {
                        out.println(num + " is an even number.<br><br>");
                    } else {
                        out.println(num + " is an odd number.<br><br>");
                    }

                    // Multiplication table
                    out.println("<h3>Multiplication Table</h3>");

                    for (int i = 0; i <= 10; i++) {
                        out.println(num + " x " + i + " = "
                                + (num * i) + "<br>");
                    }

                    // Calculate factorial
                    if (num <= 20) {
                        long fact = 1;

                        for (int i = 1; i <= num; i++) {
                            fact = fact * i;
                        }

                        out.println("<br>Factorial of " + num
                                + " is " + fact);
                    } else {
                        out.println("<br>Number is too large "
                                + "to calculate factorial using long.");
                    }
                }

            } catch (NumberFormatException e) {
                out.println("Invalid input. Please enter a valid integer.");
            }
        }
    %>

</body>
</html>
