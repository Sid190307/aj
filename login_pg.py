
import java.awt.*;
import java.awt.event.*;

class p2 implements ActionListener {

    Button login;
    TextField uname, pword;
    Label l1, l2, l3;

    p2() {
        Frame f = new Frame();

        l1 = new Label("UserName:");
        l2 = new Label("Password:");
        l3 = new Label();

        login = new Button("Login");
        uname = new TextField();
        pword = new TextField();
        pword.setEchoChar('*');

        l1.setBounds(20, 80, 100, 30);
        uname.setBounds(220, 80, 100, 30);

        l2.setBounds(20, 120, 150, 30);
        pword.setBounds(220, 120, 100, 30);

        login.setBounds(140, 170, 100, 40);
        l3.setBounds(100, 220, 200, 50);

        login.addActionListener(this);

        f.add(l1);
        f.add(l2);
        f.add(l3);
        f.add(uname);
        f.add(pword);
        f.add(login);

        f.setSize(400, 400);
        f.setTitle("Login Page");
        f.setLayout(null);
        f.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == login) {
            String username = uname.getText();
            String password = pword.getText();

            if (username.equals("admin") &&
                password.equals("p123")) {
                l3.setText("Login Successful");
            } else {
                l3.setText("Invalid Login");
            }
        }
    }

    public static void main(String[] args) {
        new p2();
    }
}
