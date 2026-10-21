use company;

create table newemp(id int(3), profile_pic Blob);

insert into newemp values(5, "C:\\Users\\Admin\\Downloads\\employee.jpg");

select * from newemp;


package jdbc;

import java.sql.*;
import java.io.*;
import javax.swing.*;

public class JDBC2 {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/company";
        String user = "root";
        String password = "root";

        String imagePath =
                "C:\\Users\\Admin\\Downloads\\images.jpg";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            try (Connection conn =
                    DriverManager.getConnection(url, user, password)) {

                System.out.println("Connected to DB");

                // Insert image into the database
                String query =
                        "INSERT INTO newemp(id, profile_pic) VALUES (?, ?)";

                try (PreparedStatement ps =
                        conn.prepareStatement(query);
                     InputStream in = new FileInputStream(imagePath)) {

                    ps.setInt(1, 1);
                    ps.setBlob(2, in);

                    ps.executeUpdate();

                    System.out.println("Image inserted successfully");
                }

                // Retrieve records from the table
                try (Statement stmt = conn.createStatement();
                     ResultSet rs =
                             stmt.executeQuery("SELECT * FROM newemp")) {

                    System.out.println("Contents of the table");

                    while (rs.next()) {

                        int id = rs.getInt("id");
                        System.out.println("ID: " + id);

                        Blob blob = rs.getBlob("profile_pic");

                        if (blob != null) {
                            byte[] imgData =
                                    blob.getBytes(1, (int) blob.length());

                            SwingUtilities.invokeLater(() -> {
                                JFrame f = new JFrame(
                                        "Employee Profile Picture - ID: " + id);

                                f.setDefaultCloseOperation(
                                        JFrame.DISPOSE_ON_CLOSE);

                                f.add(new JLabel(new ImageIcon(imgData)));
                                f.pack();
                                f.setLocationRelativeTo(null);
                                f.setVisible(true);
                            });

                            blob.free();
                        }
                    }
                }

                System.out.println("Session closed successfully");
            }

        } catch (ClassNotFoundException e) {
            System.out.println("Driver Error: " + e.getMessage());

        } catch (SQLException e) {
            System.out.println("Database Error: " + e.getMessage());

        } catch (IOException e) {
            System.out.println("File Error: " + e.getMessage());
        }
    }
}
