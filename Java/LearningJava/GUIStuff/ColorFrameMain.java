import java.awt.Color;
import java.awt. FlowLayout;
import java.awt. Font;
import java.awt.event.*;
import javax.swing.*;

public class ColorFrameMain {
    public static void main(String[] args) {
        new ColorFrame();
    }
}


class ColorFrame extends JFrame implements ActionListener{
    JButton button;
    JLabel label;

    ColorFrame() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new FlowLayout());

        button = new JButton("Pick a color");
        button.addActionListener(this);

        label = new JLabel();
        label.setBackground (Color.white);
        label.setText("This is some text.");
        label.setFont(new Font("Verdana", Font.PLAIN, 100));
        label.setOpaque(true);

        this.add(button);
        this.add(label);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
    }
@Override
public void actionPerformed(ActionEvent e) {
    
    if(e.getSource()==button) {
        new JColorChooser();
        
        Color color = JColorChooser.showDialog(null, "Pick a color...... I guess", Color.black);
        //label.setForeground(color);
        label.setBackground(color);
    }
    
}
}