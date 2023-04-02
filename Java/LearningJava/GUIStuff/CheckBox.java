
import java.awt. FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;

public class CheckBox {
    public static void main(String[] args) {
        new CheckBoxFrame();
    }
}
class CheckBoxFrame extends JFrame implements ActionListener{ 
    JButton button;
    JCheckBox checkBox;
    //ImageIcon xIcon;
    //ImageIcon checkIcon;
    CheckBoxFrame() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) ;
        this.setLayout (new FlowLayout());

        //xIcon = new ImageIcon("X.png");
        //checkIcon = new ImageIcon("checkmark.png");

        button = new JButton("Submit");
        button.addActionListener(this);
        button.setFocusable(false);

        checkBox = new JCheckBox();
        checkBox.setText("I am not a robot.");
        checkBox.setFocusable(false);
        checkBox.setFont(new Font("Comic Sans", Font.PLAIN, 25));
        //checkBox.setIcon(xIcon);
        //checkBox.setSelectedIcon(checkIcon);


        this.add(button);
        this.add(checkBox);
        this.pack();
        this.setVisible(true);
        }
    @Override
    public void actionPerformed(ActionEvent e) {
       if(e.getSource()==button){
            System.out.println(checkBox.isSelected());
       }
        
    }
}