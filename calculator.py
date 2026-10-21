
import java.awt.*;
import java.awt.event.*;

class p1 implements ActionListener {

    Button add, sub, mul, div;
    TextField fno, sno, res;
    Label l1, l2;

    p1() {
        Frame f = new Frame();

        l1 = new Label("Enter first number");
        l2 = new Label("Enter second number");

        add = new Button("+");
        sub = new Button("-");
        mul = new Button("*");
        div = new Button("/");

        fno = new TextField();
        sno = new TextField();
        res = new TextField();

        l1.setBounds(20, 80, 150, 30);
        fno.setBounds(220, 80, 100, 30);

        l2.setBounds(20, 120, 150, 30);
        sno.setBounds(220, 120, 100, 30);

        add.setBounds(20, 160, 30, 30);
        sub.setBounds(80, 160, 30, 30);
        mul.setBounds(140, 160, 30, 30);
        div.setBounds(200, 160, 30, 30);

        res.setBounds(20, 200, 150, 30);
        res.setEditable(false);

        add.addActionListener(this);
        sub.addActionListener(this);
        mul.addActionListener(this);
        div.addActionListener(this);

        f.add(l1);
        f.add(l2);
        f.add(add);
        f.add(sub);
        f.add(mul);
        f.add(div);
        f.add(fno);
        f.add(sno);
        f.add(res);

        f.setSize(500, 500);
        f.setTitle("Calculator");
        f.setLayout(null);
        f.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            int n1 = Integer.parseInt(fno.getText());
            int n2 = Integer.parseInt(sno.getText());

            double n3 = 0.0;

            if (e.getSource() == add) {
                n3 = n1 + n2;
            } else if (e.getSource() == sub) {
                n3 = n1 - n2;
            } else if (e.getSource() == mul) {
                n3 = n1 * n2;
            } else if (e.getSource() == div) {
                if (n2 == 0) {
                    res.setText("Cannot divide by zero");
                    return;
                }
                n3 = (double) n1 / n2;
            }

            res.setText(String.valueOf(n3));

        } catch (NumberFormatException ex) {
            res.setText("Enter valid numbers");
        }
    }

    public static void main(String[] args) {
        new p1();
    }
}
