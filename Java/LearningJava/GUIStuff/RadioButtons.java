

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class RadioButtons {
    public static void main(String[] args) {
        new RadioButtonsFrame();
    }
}
class RadioButtonsFrame extends JFrame implements ActionListener {

    JRadioButton pizzaButton;
    JRadioButton hamburgerButton;
    JRadioButton hotdogButton;
    
    RadioButtonsFrame() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) ;
        this.setLayout (new FlowLayout());

         pizzaButton= new JRadioButton("Pizza");
         hamburgerButton= new JRadioButton("Hamburger");
         hotdogButton= new JRadioButton("Hotdog");

         pizzaButton.addActionListener(this);
         hamburgerButton.addActionListener(this);
         hotdogButton.addActionListener(this);

        ButtonGroup group = new ButtonGroup();
        group.add(pizzaButton);
        group.add(hamburgerButton);
        group.add(hotdogButton);

        this.add(pizzaButton);
        this.add(hamburgerButton);
        this.add(hotdogButton);
        this.pack();
        this.setVisible(true);
        }

    @Override
    public void actionPerformed(ActionEvent e) {
        
        if(e.getSource()==pizzaButton) {
            System.out.println("You ordered a pizza!");
            pizzaButton.setEnabled(false);
            hamburgerButton.setEnabled(false);
            hotdogButton.setEnabled(false);
        }
        else if(e.getSource()==hamburgerButton) {
            System.out.println("You ordered a hamburger!");
            pizzaButton.setEnabled(false);
            hamburgerButton.setEnabled(false);
            hotdogButton.setEnabled(false);
        }
        else if(e.getSource()==hotdogButton) {
            System.out.println("You ordered a hotdog!");
            pizzaButton.setEnabled(false);
            hamburgerButton.setEnabled(false);
            hotdogButton.setEnabled(false);
        }
        
    }
    
}