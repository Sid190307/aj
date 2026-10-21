HTML
<!DOCTYPE html>
<html>
<head>
    <title>Check Voting Eligibility</title>
    <meta charset="UTF-8">
</head>
<body>

    <form action="Age" method="get">
        <fieldset>
            <legend>Check Your Voting Eligibility</legend>

            <label for="name">Enter Name:</label><br>
            <input type="text" id="name" name="name" required>
            <br><br>

            <label for="age">Enter Age:</label><br>
            <input type="number" id="age" name="age"
                   min="0" step="1" required>
            <br><br>

            <input type="submit" value="Check Eligibility">
        </fieldset>
    </form>

</body>
</html>

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Age")
public class Age extends HttpServlet {

    protected void processRequest(
            HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");

        try (PrintWriter out = response.getWriter()) {

            String name = request.getParameter("name");
            String agestr = request.getParameter("age");

            String message;

            if (name == null || name.trim().isEmpty()) {
                message = "Please enter your name.";
            } else if (agestr == null || agestr.trim().isEmpty()) {
                message = "Please enter your age.";
            } else {
                try {
                    int age = Integer.parseInt(agestr);

                    if (age < 0) {
                        message = "Please enter a valid age.";
                    } else if (age >= 18) {
                        message = escapeHtml(name)
                                + ", you are eligible to vote.";
                    } else {
                        message = escapeHtml(name)
                                + ", you are not eligible to vote.";
                    }

                } catch (NumberFormatException e) {
                    message = "Invalid age entered. Please try again.";
                }
            }

            out.println("<html>");
            out.println("<head><title>Voting Eligibility</title></head>");
            out.println("<body>");
            out.println("<h1>Your Voting Eligibility</h1>");
            out.println("<p>" + message + "</p>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    private String escapeHtml(String text) {
        return text.replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;")
                   .replace("\"", "&quot;")
                   .replace("'", "&#39;");
    }

    @Override
    protected void doGet(
            HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {

        processRequest(request, response);
    }
}
