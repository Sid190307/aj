
public class StudentDetailForm extends java.awt.Frame {

    /**
     * Creates new form StudentDetailForm
     */
    public StudentDetailForm() {
        initComponents();

        choice2.add("Computer Science");
        choice2.add("IT");
        choice2.add("Biotech");
        choice2.add("Life Science");

        choice4.add("FY");
        choice4.add("SY");
        choice4.add("TY");
    }

    private void button1ActionPerformed(
            java.awt.event.ActionEvent evt) {

        String s1 = textField1.getText();
        String s2 = textField2.getText();
        String s3 = textArea1.getText();

        String course = choice2.getSelectedItem();
        String classs = choice4.getSelectedItem();

        // Hobbies
        String h = "";

        if (checkbox4.getState())
            h = h + "Singing, ";

        if (checkbox5.getState())
            h = h + "Drawing, ";

        if (checkbox6.getState())
            h = h + "Dancing, ";

        if (checkbox7.getState())
            h = h + "Sports";

        // Gender
        String g = "";

        if (checkbox1.getState())
            g = "Male";
        else if (checkbox2.getState())
            g = "Female";
        else
            g = "Other";

        // Display student details
        textArea2.setText(
                "Name: " + s1 + "\n" +
                "Roll Number: " + s2 + "\n" +
                "Address: " + s3 + "\n" +
                "Favourite Course: " + course + "\n" +
                "Hobbies: " + h + "\n" +
                "Class: " + classs + "\n" +
                "Gender: " + g
        );
    }
}
