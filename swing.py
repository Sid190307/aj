Swing 1

import javax.swing.*;
import java.awt.*;

public class Swing1 extends JFrame {

    JTextField jTextField1 = new JTextField();
    JTextField jTextField2 = new JTextField();
    JTextField jTextField3 = new JTextField();

    JTextArea jTextArea1 = new JTextArea(3, 20);

    JRadioButton jRadioButton1 = new JRadioButton("Male");
    JRadioButton jRadioButton2 = new JRadioButton("Female");
    JRadioButton jRadioButton3 = new JRadioButton("Other");

    JButton jButton1 = new JButton("Next");
    JButton jButton2 = new JButton("Validate and Continue");

    public Swing1() {
        setTitle("Personal Details Form");
        setSize(550, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        ButtonGroup group = new ButtonGroup();
        group.add(jRadioButton1);
        group.add(jRadioButton2);
        group.add(jRadioButton3);

        JPanel form = new JPanel(new GridLayout(0, 2, 8, 8));
        form.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));

        form.add(new JLabel("Name:"));
        form.add(jTextField1);

        form.add(new JLabel("Email:"));
        form.add(jTextField2);

        form.add(new JLabel("Phone Number:"));
        form.add(jTextField3);

        form.add(new JLabel("Address:"));
        form.add(new JScrollPane(jTextArea1));

        JPanel genderPanel = new JPanel();
        genderPanel.add(jRadioButton1);
        genderPanel.add(jRadioButton2);
        genderPanel.add(jRadioButton3);

        form.add(new JLabel("Gender:"));
        form.add(genderPanel);

        JPanel buttons = new JPanel();
        buttons.add(jButton1);
        buttons.add(jButton2);

        add(form, BorderLayout.CENTER);
        add(buttons, BorderLayout.SOUTH);

        jButton1.addActionListener(this::jButton1ActionPerformed);
        jButton2.addActionListener(this::jButton2ActionPerformed);
    }

    private void jButton1ActionPerformed(
            java.awt.event.ActionEvent evt) {

        Swing2 bt = new Swing2();
        bt.setVisible(true);
    }

    private void jButton2ActionPerformed(
            java.awt.event.ActionEvent evt) {

        if (jTextField1.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please Enter your name");
            return;
        }

        String email = jTextField2.getText().trim();

        if (email.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please Enter your email");
            return;
        }

        if (!email.matches("^[^\\s@]+@[^\\s@]+\\.com$")) {
            JOptionPane.showMessageDialog(
                    this, "Email must have @ and .com");
            return;
        }

        String number = jTextField3.getText().trim();

        if (!number.matches("[0-9]{10}")) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter a valid 10-digit number");
            return;
        }

        if (jTextArea1.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter your address");
            return;
        }

        if (!(jRadioButton1.isSelected()
                || jRadioButton2.isSelected()
                || jRadioButton3.isSelected())) {

            JOptionPane.showMessageDialog(
                    this, "Please select your gender");
            return;
        }

        JOptionPane.showMessageDialog(this, "Personal details are valid");

        Swing2 bt = new Swing2();
        bt.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Swing1().setVisible(true));
    }
}

Swing 2

import javax.swing.*;
import java.awt.*;

public class Swing2 extends JFrame {

    JTextField jTextField1 = new JTextField();
    JTextField jTextField2 = new JTextField();

    JTextArea jTextArea1 = new JTextArea(3, 20);
    JTextArea jTextArea2 = new JTextArea(3, 20);

    JComboBox<String> jComboBox1 = new JComboBox<>(
            new String[]{
                "Select Qualification",
                "HSC",
                "Diploma",
                "Bachelor's Degree",
                "Master's Degree"
            });

    JList<String> jList1 = new JList<>(
            new String[]{
                "C",
                "C++",
                "Java",
                "Python",
                "JavaScript",
                "PHP"
            });

    JButton jButton1 = new JButton("Submit");

    public Swing2() {
        setTitle("Professional Details Form");
        setSize(600, 550);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel form = new JPanel(new GridLayout(0, 2, 8, 8));
        form.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));

        form.add(new JLabel("Specialisation:"));
        form.add(jTextField1);

        form.add(new JLabel("Experience:"));
        form.add(jTextField2);

        form.add(new JLabel("Achievements:"));
        form.add(new JScrollPane(jTextArea1));

        form.add(new JLabel("Projects:"));
        form.add(new JScrollPane(jTextArea2));

        form.add(new JLabel("Qualification:"));
        form.add(jComboBox1);

        jList1.setSelectionMode(
                ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);

        form.add(new JLabel("Programming Languages:"));
        form.add(new JScrollPane(jList1));

        JPanel buttons = new JPanel();
        buttons.add(jButton1);

        add(form, BorderLayout.CENTER);
        add(buttons, BorderLayout.SOUTH);

        jButton1.addActionListener(this::jButton1ActionPerformed);
    }

    private void jButton1ActionPerformed(
            java.awt.event.ActionEvent evt) {

        if (jTextField1.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter your specialisation");
            return;
        }

        if (jTextField2.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter your experience");
            return;
        }

        if (jTextArea1.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter your achievements");
            return;
        }

        if (jTextArea2.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Please Enter your projects");
            return;
        }

        if (jComboBox1.getSelectedIndex() == 0) {
            JOptionPane.showMessageDialog(
                    this, "Select Qualification");
            return;
        }

        if (jList1.isSelectionEmpty()) {
            JOptionPane.showMessageDialog(
                    this, "Select Programming Language");
            return;
        }

        JOptionPane.showMessageDialog(
                this, "Form Filled and Submitted");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Swing2().setVisible(true));
    }
}
