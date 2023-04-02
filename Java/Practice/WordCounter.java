package Practice;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class WordCounter {
    public static void main(String[] args) {
        new ActualWordCounter();
    }
    
}
class ActualWordCounter extends JFrame implements ActionListener{

    JTextField tf;
    JLabel l;
    JButton b;
    JPanel p;
    JLabel words = new JLabel(); //has to be this way. IDK Why
    ActualWordCounter(){
        // create the frame
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500,500);
        this.setTitle("Word Counter");
        this.setLayout(null);

        // Creates the label
        l = new JLabel("Enter a paragraph for a word count: ");
        l.setBounds(150,25,400,15);
        l.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        l.setHorizontalTextPosition(JLabel.CENTER);

        // Creates the textField
        tf = new JTextField();
        tf.setBounds(50,50,400,25);
        tf.setFont(new Font("Comic Sans", Font.PLAIN, 15));
        tf.setForeground(Color.CYAN);
        tf.setCaretColor(Color.BLACK);

        // Creates the submit button
        b = new JButton("Submit");
        b.setBounds(200,80,75,25);
        b.setFocusable(false);
        b.addActionListener(this);
        
        // Creates the panel to hold all items
        p =new JPanel();
        p.setPreferredSize(new Dimension(500,500));
        p.setBounds(0,0,500,500);
        p.setLayout(null);
        p.add(l);
        p.add(tf);
        p.add(b);

        // Adds panel to the frame and sets visible
        this.add(p);
        this.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==b){
            String para = tf.getText();
            tf.setEditable(false);
            int count = 1;

            // Increments count whenever the program finds a space
            for(int i = 0; i<para.length();i++){
                if(para.charAt(i)==' '){
                    count++;
                }
            }

            // IDK why it had to loop twice but it works. *Shrugs*
            for(int j=0;j<2;j++) {
                words.setText("Your paragraph has " + count + " word(s). "); //has to be this way dont ask me why
                words.setBounds(150,125,400,15);
                words.setFont(new Font("Times New Roman", Font.PLAIN, 15));
                words.setHorizontalTextPosition(JLabel.CENTER);
                p.add(words);
            }
        }
        p.setVisible(true);
    }
}