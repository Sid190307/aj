
import java.io.*;
import java.sql.*;

class p1 {

    public static void main(String args[]) {

        String url = "jdbc:mysql://localhost:3306/company";
        String user = "root";
        String password = "root";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            try (
                Connection con =
                    DriverManager.getConnection(url, user, password);

                PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO user420 VALUES (?, ?, ?)");

                BufferedReader br = new BufferedReader(
                    new InputStreamReader(System.in))
            ) {

                con.setAutoCommit(false);

                while (true) {

                    System.out.print("Enter ID: ");
                    int id = Integer.parseInt(br.readLine());

                    System.out.print("Enter Name: ");
                    String name = br.readLine();

                    System.out.print("Enter Salary: ");
                    int salary = Integer.parseInt(br.readLine());

                    ps.setInt(1, id);
                    ps.setString(2, name);
                    ps.setInt(3, salary);

                    ps.executeUpdate();

                    System.out.print("Enter commit/rollback: ");
                    String ans = br.readLine();

                    if (ans.equalsIgnoreCase("commit")) {
                        con.commit();
                        System.out.println(
                            "Transaction Committed Successfully.");
                    } else if (ans.equalsIgnoreCase("rollback")) {
                        con.rollback();
                        System.out.println(
                            "Transaction Rolled Back Successfully.");
                    } else {
                        System.out.println(
                            "Invalid choice. Transaction remains pending.");
                    }

                    System.out.print(
                        "Want to add more records? (y/n): ");
                    String res = br.readLine();

                    if (res.equalsIgnoreCase("n")) {
                        break;
                    }
                }

                System.out.println("Session Closed Successfully.");
            }

        } catch (ClassNotFoundException e) {
            System.out.println("Driver Error: " + e.getMessage());

        } catch (SQLException e) {
            System.out.println("Database Error: " + e.getMessage());

        } catch (IOException e) {
            System.out.println("Input Error: " + e.getMessage());

        } catch (NumberFormatException e) {
            System.out.println(
                "Please enter valid numeric values.");
        }
    }
}


use company;

create table user420(id int(3), name varchar(20), salary int(7));


select * from user420;


