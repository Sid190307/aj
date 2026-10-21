create database company;

use company;

create table emp(id int(2), name varchar(20), salary int(6));

insert into emp values(1, "SRK", 9000000);

insert into emp values(2, "ABD", 700000);



package jdbc;

import java.sql.*;

public class JDBC {

    public static void main(String[] args) {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/company",
                    "root",
                    "root"
            );

            Statement stmt = con.createStatement();

            // Display existing records
            System.out.println("Initial Records:");
            displayRecords(stmt);

            // Insert a record
            stmt.executeUpdate(
                    "INSERT INTO emp VALUES (3, 'KA', 70000)"
            );

            System.out.println("After Inserting Record:");
            displayRecords(stmt);

            // Update a record
            stmt.executeUpdate(
                    "UPDATE emp SET id = 4 WHERE id = 3"
            );

            System.out.println("After Updating Record:");
            displayRecords(stmt);

            // Delete a record
            stmt.executeUpdate(
                    "DELETE FROM emp WHERE name = 'KA'"
            );

            System.out.println("After Deleting Record:");
            displayRecords(stmt);

            // Display table and column metadata
            ResultSet rs = stmt.executeQuery("SELECT * FROM emp");

            ResultSetMetaData rsMD = rs.getMetaData();

            System.out.println(
                    "Table Name: " + rsMD.getTableName(1)
            );

            for (int i = 1; i <= rsMD.getColumnCount(); i++) {
                System.out.println(
                        "Column Name: " + rsMD.getColumnName(i)
                );
            }

            rs.close();
            stmt.close();
            con.close();

            System.out.println("Database operations completed successfully");

        } catch (Exception e) {
            System.out.println(e);
        }
    }

    // Method to display all employee records
    public static void displayRecords(Statement stmt)
            throws SQLException {

        ResultSet rs = stmt.executeQuery("SELECT * FROM emp");

        while (rs.next()) {
            System.out.println(
                    rs.getInt(1) + " " +
                    rs.getString(2) + " " +
                    rs.getInt(3)
            );
        }

        rs.close();
    }
}
