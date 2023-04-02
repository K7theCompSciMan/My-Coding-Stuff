
import java.awt.Color;
import java.awt.Font;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.border.Border;

public class LabelStuff {
    public static void main(String[] args) {

        ImageIcon image = new ImageIcon("IMG.jpg");

        Border border = BorderFactory.createLineBorder(Color.green,3);

        JLabel label = new JLabel(); //creates a label

        label.setText("Do You Even Code Bro??"); //sets text of the label

        label.setHorizontalTextPosition(JLabel.CENTER); //set text left, center, or right of image

        label.setVerticalTextPosition(JLabel.TOP); //set text top, center, or bottom

        label.setForeground(Color.blue); //sets text color

        label.setFont(new Font("MV Boli", Font.PLAIN, 20)); //sets font of text

        label.setIconTextGap(100); //sets gap b/w Icon and text

        label.setBackground(Color.black); //sets background color

        label.setOpaque(true); //displays background color

        label.setBorder(border);

        label.setVerticalAlignment(JLabel.CENTER); //sets vertical pos of icon+text

        label.setHorizontalAlignment(JLabel.CENTER); //sets horizontal pos of icon+text

        //label.setBounds(100,100,500,500); //sets x,y and dimensions


        label.setIcon(image); //sets the image
      







        JFrame frame = new JFrame();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //frame.setSize(500, 500);

        //frame.setLayout(null);

        frame.setVisible(true);

        frame.add(label);

        frame.pack(); //size of frame adjusts to fit the size of whats inside **ADD EVERYTHING BEFORE**
        
    }
}
