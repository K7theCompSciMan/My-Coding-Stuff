package Practice;


import javax.swing.*;
import java.awt.event.*;
import java.io.File;

public class ButtonWithFileChooser extends JButton implements ActionListener{
    
    JFileChooser chooser;
    public File filepath;
    
    public ButtonWithFileChooser(){
        this.setText("Select File");
        this.setFocusable(false);
        this.addActionListener(null);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==this) {

            JFileChooser fileChooser = new JFileChooser();

            fileChooser.setCurrentDirectory(new File("."));

            int response = fileChooser.showOpenDialog(null); //selects file to open 
            
            //int response = fileChooser.showSaveDialog(null); //selects file to save

            if(response ==JFileChooser.APPROVE_OPTION) {
                filepath = new File(fileChooser.getSelectedFile().getAbsolutePath());
            }
            
        }
        
    }
}