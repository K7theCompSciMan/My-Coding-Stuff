package Practice;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUICalculator extends JFrame implements ActionListener {
    static JFrame f;
    static JTextField l;

    String s0,s1,s2;
    GUICalculator() {
        s0 = s1 = s2 = "";
    }
    public static void main(String[] args) {

        GUICalculator c = new GUICalculator();

        f = new JFrame("GUI Calculator");
        f.setLayout(null);
        l = new JTextField(16);
        l.setEditable(false);

        JButton b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,bdec,ba,bs,bd,bm,bc,be;

        b0 = new JButton("0");
        b1 = new JButton("1");
        b2 = new JButton("2");
        b3 = new JButton("3");
        b4 = new JButton("4");
        b5 = new JButton("5");
        b6 = new JButton("6");
        b7 = new JButton("7");
        b8 = new JButton("8");
        b9 = new JButton("9");
        bdec = new JButton(".");

        ba = new JButton("+");
        bs = new JButton("-");
        bd = new JButton("/");
        bm = new JButton("*");
        bc = new JButton("C");

        be = new JButton("=");
        
        b0.setFocusable(false);
        b1.setFocusable(false);
        b2.setFocusable(false);
        b3.setFocusable(false);
        b4.setFocusable(false);
        b5.setFocusable(false);
        b6.setFocusable(false);
        b7.setFocusable(false);
        b8.setFocusable(false);
        b9.setFocusable(false);
        bdec.setFocusable(false);
        ba.setFocusable(false);
        bs.setFocusable(false);
        bm.setFocusable(false);
        bd.setFocusable(false);
        bc.setFocusable(false);
        be.setFocusable(false);




        JPanel p = new JPanel();
        p.setBounds(10,0,300,25);
        JPanel bp = new JPanel();
        bp.setBounds(0,30,300,300);
        bp.setLayout(new GridLayout(5,4));

        bm.addActionListener(c);
        bd.addActionListener(c);
        bs.addActionListener(c);
        ba.addActionListener(c);
        b9.addActionListener(c);
        b8.addActionListener(c);
        b7.addActionListener(c);
        b6.addActionListener(c);
        b5.addActionListener(c);
        b4.addActionListener(c);
        b3.addActionListener(c);
        b2.addActionListener(c);
        b1.addActionListener(c);
        b0.addActionListener(c);
        be.addActionListener(c);
        bc.addActionListener(c);
        bdec.addActionListener(c);

        p.add(l);
        bp.add(b0);
        bp.add(b1);
        bp.add(b2);
        bp.add(b3);
        bp.add(ba);
        bp.add(b4);
        bp.add(b5);
        bp.add(b6);
        bp.add(bs);
        bp.add(b7);
        bp.add(b8);
        bp.add(b9);
        bp.add(bm);
        bp.add(bdec);
        bp.add(b0);
        bp.add(bc);
        bp.add(bd);
        bp.add(be);

        f.add(p);
        f.add(bp);
        f.setSize(312,310);
        f.setVisible(true);
        

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String inp = e.getActionCommand();

        if ((inp.charAt(0) >= '0' && inp.charAt(0) <= '9') || inp.charAt(0) == '.') {
            if (!s1.equals("")) {
                s2 = s2 + inp;
            }
            else {
                s0 = s0 + inp;
            }
            l.setText(s0 + s1 + s2);
        }
        else if (inp.charAt(0) == 'C') {

            s0 = s1 = s2 = "";
         
            l.setText(s0 + s1 + s2);
        }
        else if (inp.charAt(0) == '=') {
 
            double te;

            if (s1.equals("+")) {
                te = (Double.parseDouble(s0) + Double.parseDouble(s2));
            }
            else if (s1.equals("-")) {
                te = (Double.parseDouble(s0) - Double.parseDouble(s2));
            }
            else if (s1.equals("/")) {
                te = (Double.parseDouble(s0) / Double.parseDouble(s2));
            }
            else {
                te = (Double.parseDouble(s0) * Double.parseDouble(s2));
            }
 
            l.setText(s0 + s1 + s2 + "=" + te);

            s0 = Double.toString(te);
 
            s1 = s2 = "";
        }
        else {
            if (s1.equals("") || s2.equals("")) {
                s1 = inp;
            }
            else {
                double te;
 
                if (s1.equals("+")) {
                    te = (Double.parseDouble(s0) + Double.parseDouble(s2)); 
                }
                else if (s1.equals("-")) {
                    te = (Double.parseDouble(s0) - Double.parseDouble(s2));
                }
                else if (s1.equals("/")){
                    te = (Double.parseDouble(s0) / Double.parseDouble(s2));
                }
                else {
                    te = (Double.parseDouble(s0) * Double.parseDouble(s2));
                }

                s0 = Double.toString(te);
 
                s1 = inp;
 
                s2 = "";
            }
 
            l.setText(s0 + s1 + s2);
        }
        
    }
}
