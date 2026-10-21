
<!DOCTYPE html>
<html>
<head>
    <title>Book Details</title>
    <meta charset="UTF-8">
</head>
<body>

    <h1>Enter Book Details</h1>

    <form action="Bookdetails" method="post">
        <table>
            <tr>
                <td>Title:</td>
                <td>
                    <input type="text" name="title" required>
                </td>
            </tr>

            <tr>
                <td>Author:</td>
                <td>
                    <input type="text" name="author" required>
                </td>
            </tr>

            <tr>
                <td>Year of Publication:</td>
                <td>
                    <input type="number" name="year"
                           min="1" step="1" required>
                </td>
            </tr>

            <tr>
                <td>ISBN:</td>
                <td>
                    <input type="text" name="isbn"
                           pattern="[0-9]+" required>
                </td>
            </tr>

            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Submit">
                </td>
            </tr>
        </table>
    </form>

</body>
</html>


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;

@WebServlet("/Bookdetails")
public class Bookdetails extends HttpServlet {

    private static final long serialVersionUID = 1L;

    @Override
    protected void doPost(
            HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");

        String title = request.getParameter("title");
        String author = request.getParameter("author");
        String year = request.getParameter("year");
        String isbn = request.getParameter("isbn");

        try (PrintWriter out = response.getWriter()) {

            try {
                int publicationYear = Integer.parseInt(year);
                long isbnNumber = Long.parseLong(isbn);

                Class.forName("com.mysql.cj.jdbc.Driver");

                String url = "jdbc:mysql://localhost:3306/mydb";

                try (Connection conn =
                        DriverManager.getConnection(url, "root", "root")) {

                    // Insert book details
                    String insertSQL =
                            "INSERT INTO books "
                            + "(title, author, `year`, isbn) "
                            + "VALUES (?, ?, ?, ?)";

                    try (PreparedStatement pstmt =
                            conn.prepareStatement(insertSQL)) {

                        pstmt.setString(1, title);
                        pstmt.setString(2, author);
                        pstmt.setInt(3, publicationYear);
                        pstmt.setLong(4, isbnNumber);

                        pstmt.executeUpdate();
                    }

                    // Retrieve all book records
                    String selectSQL =
                            "SELECT title, author, `year`, isbn FROM books";

                    try (PreparedStatement pstmt =
                            conn.prepareStatement(selectSQL);
                         ResultSet rs = pstmt.executeQuery()) {

                        out.println("<html>");
                        out.println("<head><title>Book Details</title></head>");
                        out.println("<body>");
                        out.println("<h1>Book Details</h1>");

                        out.println("<table border='1'>");
                        out.println("<tr>");
                        out.println("<th>Title</th>");
                        out.println("<th>Author</th>");
                        out.println("<th>Year of Publication</th>");
                        out.println("<th>ISBN</th>");
                        out.println("</tr>");

                        while (rs.next()) {
                            out.println("<tr>");

                            out.println("<td>"
                                    + escapeHTML(rs.getString("title"))
                                    + "</td>");

                            out.println("<td>"
                                    + escapeHTML(rs.getString("author"))
                                    + "</td>");

                            out.println("<td>"
                                    + rs.getInt("year")
                                    + "</td>");

                            out.println("<td>"
                                    + rs.getLong("isbn")
                                    + "</td>");

                            out.println("</tr>");
                        }

                        out.println("</table>");
                        out.println("<br>");
                        out.println("<a href='index.html'>Go Back</a>");
                        out.println("</body>");
                        out.println("</html>");
                    }
                }

            } catch (NumberFormatException e) {
                out.println("<h2>Invalid Year or ISBN</h2>");

            } catch (ClassNotFoundException e) {
                out.println("<h2>MySQL Driver Not Found</h2>");

            } catch (SQLException e) {
                out.println("<h2>Database Error</h2>");
                out.println("<p>" + escapeHTML(e.getMessage()) + "</p>");
            }
        }
    }

    private String escapeHTML(String text) {
        if (text == null) {
            return "";
        }

        return text.replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;")
                   .replace("\"", "&quot;")
                   .replace("'", "&#39;");
    }
}

