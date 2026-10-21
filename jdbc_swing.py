create database student;

use student;

create table studentinfo (firstname varchar(20), lastname varchar(20), sid int(3), password int(10), address varchar(30));

insert into studentinfo values("raj", "sharma", 1, 1234, "Sion");


import java.sql.*;
import javax.swing.JOptionPane;

private void detailsbuttonActionPerformed(
        java.awt.event.ActionEvent evt) {

    String id = sidtext.getText().trim();

    if (id.isEmpty()) {
        JOptionPane.showMessageDialog(
                this, "Please Enter Student ID");
        return;
    }

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/student";

        try (Connection con =
                     DriverManager.getConnection(url, "root", "root");

             PreparedStatement ps = con.prepareStatement(
                     "SELECT * FROM studentinfo WHERE sid = ?")) {

            ps.setString(1, id);

            try (ResultSet rs = ps.executeQuery()) {

                if (rs.next()) {
                    String firstname = rs.getString("firstname");
                    String lastname = rs.getString("lastname");
                    String sid = rs.getString("sid");
                    String password = rs.getString("password");
                    String address = rs.getString("address");

                    fn.setText(firstname);
                    ln.setText(lastname);
                    sidtext.setText(sid);
                    pwd.setText(password);
                    add.setText(address);

                } else {
                    JOptionPane.showMessageDialog(
                            this, "Student Not Found");
                }
            }
        }

    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(
                this, "Error: " + e.getMessage());
    }
}
private void insertbuttonActionPerformed(
        java.awt.event.ActionEvent evt) {

    String id = sidtext.getText().trim();
    String firstname = fn.getText().trim();
    String lastname = ln.getText().trim();
    String password = pwd.getText();
    String address = add.getText().trim();

    if (id.isEmpty() || firstname.isEmpty()
            || lastname.isEmpty() || password.isEmpty()
            || address.isEmpty()) {

        JOptionPane.showMessageDialog(
                this, "Please Fill All Fields");
        return;
    }

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/student";

        try (Connection con =
                     DriverManager.getConnection(url, "root", "root");

             PreparedStatement ps = con.prepareStatement(
                     "INSERT INTO studentinfo "
                     + "(firstname, lastname, sid, password, address) "
                     + "VALUES (?, ?, ?, ?, ?)")) {

            ps.setString(1, firstname);
            ps.setString(2, lastname);
            ps.setString(3, id);
            ps.setString(4, password);
            ps.setString(5, address);

            int rows = ps.executeUpdate();

            if (rows > 0) {
                JOptionPane.showMessageDialog(
                        this, "Inserted Successfully");
            } else {
                JOptionPane.showMessageDialog(
                        this, "Not Inserted Successfully");
            }
        }

    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(
                this, "Error: " + e.getMessage());
    }
}
private void updatebuttonActionPerformed(
        java.awt.event.ActionEvent evt) {

    String id = sidtext.getText().trim();
    String firstname = fn.getText().trim();
    String lastname = ln.getText().trim();
    String password = pwd.getText();
    String address = add.getText().trim();

    if (id.isEmpty()) {
        JOptionPane.showMessageDialog(
                this, "Please Enter Student ID");
        return;
    }

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/student";

        try (Connection con =
                     DriverManager.getConnection(url, "root", "root");

             PreparedStatement ps = con.prepareStatement(
                     "UPDATE studentinfo "
                     + "SET firstname = ?, lastname = ?, "
                     + "password = ?, address = ? WHERE sid = ?")) {

            ps.setString(1, firstname);
            ps.setString(2, lastname);
            ps.setString(3, password);
            ps.setString(4, address);
            ps.setString(5, id);

            int rows = ps.executeUpdate();

            if (rows > 0) {
                JOptionPane.showMessageDialog(
                        this, "Updated Successfully");
            } else {
                JOptionPane.showMessageDialog(
                        this, "Student Not Found or Not Updated");
            }
        }

    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(
                this, "Error: " + e.getMessage());
    }
}
private void deletebuttonActionPerformed(
        java.awt.event.ActionEvent evt) {

    String id = sidtext.getText().trim();

    if (id.isEmpty()) {
        JOptionPane.showMessageDialog(
                this, "Please Enter Student ID");
        return;
    }

    int option = JOptionPane.showConfirmDialog(
            this,
            "Do you want to delete this student?",
            "Confirmation",
            JOptionPane.YES_NO_OPTION
    );

    if (option != JOptionPane.YES_OPTION) {
        return;
    }

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");

        String url = "jdbc:mysql://localhost:3306/student";

        try (Connection con =
                     DriverManager.getConnection(url, "root", "root");

             PreparedStatement ps = con.prepareStatement(
                     "DELETE FROM studentinfo WHERE sid = ?")) {

            ps.setString(1, id);

            int rows = ps.executeUpdate();

            if (rows > 0) {
                fn.setText("");
                ln.setText("");
                sidtext.setText("");
                pwd.setText("");
                add.setText("");

                JOptionPane.showMessageDialog(
                        this, "Deleted Successfully");
            } else {
                JOptionPane.showMessageDialog(
                        this, "Student Not Found or Not Deleted");
            }
        }

    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(
                this, "Error: " + e.getMessage());
    }
}
private void resetbuttonActionPerformed(
        java.awt.event.ActionEvent evt) {

    fn.setText("");
    ln.setText("");
    sidtext.setText("");
    pwd.setText("");
    add.setText("");

    JOptionPane.showMessageDialog(
            this, "Fields Reset Successfully");
}
