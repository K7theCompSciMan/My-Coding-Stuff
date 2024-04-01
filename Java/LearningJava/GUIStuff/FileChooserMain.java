import java.awt.event.*;
import java.io.File;

import javax.swing.*;
import java.awt.*;
public class FileChooserMain {
    public static void main(String[] args) {
        new FileChooser();
    }
}
class FileChooser extends JFrame implements ActionListener {
   JButton b;
   
    FileChooser() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) ;
        this.setLayout(new FlowLayout());

        b = new JButton("Select File");
        b.addActionListener(this);

        this.add(b);
        this.pack();
        this.setVisible(true);
        
    }

    @Override
    public void actionPerformed (ActionEvent e) {
        if(e.getSource()==b) {

            JFileChooser fileChooser = new JFileChooser();

            fileChooser.setCurrentDirectory(new File("."));

            //int response = fileChooser.showOpenDialog(null); //selects file to open 
            
            int response = fileChooser.showSaveDialog(null); //selects file to save

            if(response ==JFileChooser.APPROVE_OPTION) {
                File file = new File(fileChooser.getSelectedFile().getAbsolutePath());
                System.out.println(file);
            }
            
        }
    }
}
