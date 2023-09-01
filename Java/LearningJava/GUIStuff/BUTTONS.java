import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class BUTTONS {
    public static void main(String[] args) {
        
       new MyFrame();
    }
}



class MyFrame extends JFrame implements ActionListener{

        JButton button;
        JLabel label;
    
    
        MyFrame(){

            ImageIcon icon = new ImageIcon("IMG.jpg");

            label = new JLabel();
            label.setText("Do you like Dr. Stone??");
            label.setBounds(150,250,150,150);
            label.setOpaque(true);
            label.setVisible(false);

            button = new JButton();
            button.setBounds(100,100,250,100);
            //button.addActionListener(e -> System.out.println("DOCTOR STONE!")); //other way other than importing ActionListener
            button.setText("DOCTOR STONE!");
            button.setFocusable(false);
            button.setIcon(icon);
            button.setHorizontalTextPosition(JButton.CENTER);
            button.setFont(new Font("Comic Sans", Font.ITALIC,25));
            button.setForeground(Color.black);
            button.setBackground(Color.lightGray);
            button.setBorder(BorderFactory.createEtchedBorder());
            button.setEnabled(true);


            this.setTitle("JFrame title goes here"); //sets the title of frame

            this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //exit out of application

            this.setResizable(false); //doesn't allow resizing

            this.setSize(500,500); //sets (x,y) dimension of frame

            this.setVisible(true); //makes frame visible
            
            ImageIcon image = new ImageIcon("IMG.jpg"); //creates an image icon

            this.setIconImage(image.getImage()); //sets icon to image

            this.getContentPane().setBackground(new Color(123,50,250));  //changes bg color ****Good Color

            this.add(button);
            
            this.add(label);
    }

        @Override
        public void actionPerformed(ActionEvent e) {
            if(e.getSource()==button) {
                System.out.println("DOCTOR STONE!");
                label.setVisible(true);
            }
        }
    
}