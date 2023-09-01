
//import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.Color;

public class PanelStuff {
    public static void main(String[] args) {

        JLabel label = new JLabel();
            label.setText("Hi");
            label.setVerticalAlignment(JLabel.TOP);
            label.setBounds(15,0,75,75);
        
        JPanel redPanel = new JPanel();
            redPanel.setBackground(Color.red);
            redPanel.setBounds(0,0,250,250);
            redPanel.add(label); //can move this to any panel
            

        JPanel bluePanel = new JPanel();
            bluePanel.setBackground(Color.blue);
            bluePanel.setBounds(250,0,250,250);
            bluePanel.setLayout(null);

        JPanel greenPanel = new JPanel();
            greenPanel.setBackground(Color.green);
            greenPanel.setBounds(0,250,500,250);
            greenPanel.setLayout(null); 
            
        
        
        JFrame frame = new JFrame();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLayout(null);
            frame.setSize(500, 500);
            frame.setVisible(true);
            frame.add(redPanel);
            frame.add(bluePanel);
            frame.add(greenPanel);

    }
}
