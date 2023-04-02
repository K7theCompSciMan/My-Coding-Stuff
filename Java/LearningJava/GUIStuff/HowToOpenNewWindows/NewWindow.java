package HowToOpenNewWindows;

import java.awt.Font;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class NewWindow {
    
    JFrame frame = new JFrame();
    JLabel label = new JLabel("Hello!");

    NewWindow(){   
        label.setBounds(0,0,420,420);
        label.setFont(new Font("Comic Sans", Font.ITALIC, 25));
        label.setHorizontalAlignment(JLabel.CENTER);
        label.setVerticalAlignment(JLabel.CENTER);

        frame.add(label);        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(420,420);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}