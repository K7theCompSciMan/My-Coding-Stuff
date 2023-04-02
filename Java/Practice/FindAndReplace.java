package Practice;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class FindAndReplace {
    public static void main(String[] args) {
        new ActualFindAndReplaceThingie();
    }
}
class ActualFindAndReplaceThingie extends JFrame implements ActionListener {
    JTextField tfp;
    JTextField tff;
    JTextField tfr;
    JLabel l;
    JButton b;
    JPanel p;
    JLabel words = new JLabel(); 
    String finalPara = "";
    String para;
    char[] parach;
    String find;
    char[] findch;
    String replace;
    char[] replch;


    ActualFindAndReplaceThingie(){
        // create the frame
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500,500);
        this.setTitle("Word Counter");
        this.setLayout(null);

        // Creates the label
        l = new JLabel("Enter a paragraph with a word you want to replace: ");
        l.setBounds(75,25,400,15);
        l.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        l.setHorizontalTextPosition(JLabel.CENTER);

        // Creates the textField
        tfp = new JTextField("Enter the paragraph");
        tfp.setBounds(50,50,400,25);
        tfp.setFont(new Font("Comic Sans", Font.PLAIN, 15));
        tfp.setForeground(Color.CYAN);
        tfp.setCaretColor(Color.BLACK);

        tff = new JTextField("Enter a three letter word to find (case sensitive)");
        tff.setBounds(50,75,400,25);
        tff.setFont(new Font("Comic Sans", Font.PLAIN, 15));
        tff.setForeground(Color.CYAN);
        tff.setCaretColor(Color.BLACK);

        tfr = new JTextField("Enter a three letter word to replace");
        tfr.setBounds(50,100,400,25);
        tfr.setFont(new Font("Comic Sans", Font.PLAIN, 15));
        tfr.setForeground(Color.CYAN);
        tfr.setCaretColor(Color.BLACK);

        // Creates the submit button
        b = new JButton("Submit");
        b.setBounds(200,150,75,25);
        b.setFocusable(false);
        b.addActionListener(this);
        
        // Creates the panel to hold all items
        p =new JPanel();
        p.setPreferredSize(new Dimension(500,500));
        p.setBounds(0,0,500,500);
        p.setLayout(null);
        p.add(l);
        p.add(tfp);
        p.add(tff);
        p.add(tfr);
        p.add(b);

        // Adds panel to the frame and sets visible
        this.add(p);
        this.setVisible(true);
    
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==b){
            para = tfp.getText();
            parach = para.toCharArray();
            find = tff.getText();
            findch = find.toCharArray();
            replace = tfr.getText();
            replch = replace.toCharArray();
            for(int i = 0; i<parach.length; i++){
                if(parach[i]==findch[0] && parach[i+1]==findch[1] && parach[i+2]==findch[2]){

                    parach[i] = replch[0];
                    parach[i+1] = replch[1];
                    parach[i+2] = replch[2];
                }
            }
            for(char c:parach){
                finalPara+=c;
            }
        }
        tfp.setText("");
        tfp.setText(finalPara);
    }
}