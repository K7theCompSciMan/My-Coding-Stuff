

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ComboBoxes  {
    public static void main(String[] args) {
        new ComboFrame();
    }
}
class ComboFrame extends JFrame implements ActionListener{
    
    JComboBox comboBox;
    

    ComboFrame() {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new FlowLayout());

        String [] animals = {"Dog", "Cat", "Bird"};
        comboBox = new JComboBox(animals);
        comboBox.addActionListener(this);
        //comboBox.setEditable(true);
        //System.out.println(comboBox.getItemCount());
        //comboBox.addItem("Horse");
        //comboBox.insertItemAt("Pig", 0);
        //comboBox.setSelectedIndex(0);
        //comboBox.removeItem("Bird");
        //comboBox.removeItemAt(0);
        //comboBox.removeAllItems();

        this.add(comboBox);
        this.pack();
        this.setVisible(true);
    }

    @Override
    public void actionPerformed (ActionEvent e) {
        if(e.getSource()==comboBox) {
            System.out.println(comboBox.getSelectedIndex());
            //System.out.println(comboBox.getSelectedItem());
        }
    }
}