
import java.awt.*;
import javax.swing.*;
public class NumpadStuff {
    public static void main(String[] args) {
       JFrame frame = new JFrame();

       NUMPADFlowLayout numpad = new NUMPADFlowLayout();
       NUMPADGridLayout numpadGrid = new NUMPADGridLayout();
       
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(500,500);
       frame.setResizable(false);
       frame.add(numpad,BorderLayout.EAST);
       frame.add(numpadGrid, BorderLayout.WEST);
       frame.setVisible(true);
    }
}



class NUMPADGridLayout extends JPanel {
    JButton button1;
    JButton button2;
    JButton button3;
    JButton button4;
    JButton button5;
    JButton button6;
    JButton button7;
    JButton button8;
    JButton button9;
    NUMPADGridLayout(){
        button1 = new JButton("1");
        button1.setFocusable(false);
        button1.addActionListener(e -> System.out.println("1"));

        button2 = new JButton("2");
        button2.setFocusable(false);
        button2.addActionListener(e -> System.out.println("2"));

        button3 = new JButton("3");
        button3.setFocusable(false);
        button3.addActionListener(e -> System.out.println("3"));

        button4 = new JButton("4");
        button4.setFocusable(false);
        button4.addActionListener(e -> System.out.println("4"));

        button5 = new JButton("5");
        button5.setFocusable(false);
        button5.addActionListener(e -> System.out.println("5"));

        button6 = new JButton("6");
        button6.setFocusable(false);
        button6.addActionListener(e -> System.out.println("6"));

        button7 = new JButton("7");
        button7.setFocusable(false);
        button7.addActionListener(e -> System.out.println("7"));

        button8 = new JButton("8");
        button8.setFocusable(false);
        button8.addActionListener(e -> System.out.println("8"));

        button9 = new JButton("9");
        button9.setFocusable(false);
        button9.addActionListener(e -> System.out.println("9"));

        this.setLayout(new GridLayout(3,3,5,10));
        this.setBackground(Color.yellow);
        this.setPreferredSize(new Dimension(150,150));

        this.add(button1);
        this.add(button2);
        this.add(button3);
        this.add(button4);
        this.add(button5);
        this.add(button6);
        this.add(button7);
        this.add(button8);
        this.add(button9);
    }
}
class NUMPADFlowLayout extends JPanel {
    
    JButton button1;
    JButton button2;
    JButton button3;
    JButton button4;
    JButton button5;
    JButton button6;
    JButton button7;
    JButton button8;
    JButton button9;

    
    NUMPADFlowLayout(){
        button1 = new JButton("1");
        button1.setFocusable(false);
        button1.addActionListener(e -> System.out.println("1"));

        button2 = new JButton("2");
        button2.setFocusable(false);
        button2.addActionListener(e -> System.out.println("2"));

        button3 = new JButton("3");
        button3.setFocusable(false);
        button3.addActionListener(e -> System.out.println("3"));

        button4 = new JButton("4");
        button4.setFocusable(false);
        button4.addActionListener(e -> System.out.println("4"));

        button5 = new JButton("5");
        button5.setFocusable(false);
        button5.addActionListener(e -> System.out.println("5"));

        button6 = new JButton("6");
        button6.setFocusable(false);
        button6.addActionListener(e -> System.out.println("6"));

        button7 = new JButton("7");
        button7.setFocusable(false);
        button7.addActionListener(e -> System.out.println("7"));

        button8 = new JButton("8");
        button8.setFocusable(false);
        button8.addActionListener(e -> System.out.println("8"));

        button9 = new JButton("9");
        button9.setFocusable(false);
        button9.addActionListener(e -> System.out.println("9"));

        this.setBackground(Color.yellow);

        this.setPreferredSize(new Dimension(150,50));

        this.add(button1);
        this.add(button2);
        this.add(button3);
        this.add(button4);
        this.add(button5);
        this.add(button6);
        this.add(button7);
        this.add(button8);
        this.add(button9);
    }

}
