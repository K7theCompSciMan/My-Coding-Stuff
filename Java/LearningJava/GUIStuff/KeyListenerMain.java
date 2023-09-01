import java.awt.Color;
import java.awt.event.*;
import javax.swing.*;

public class KeyListenerMain {
    public static void main(String[] args) {
        new KeyListenerFrame();
    }
}


class KeyListenerFrame extends JFrame implements KeyListener{
    
    JLabel label;
    KeyListenerFrame(){
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(500,500);
        this.setLayout(null);
        this.addKeyListener(this);

        label = new JLabel("Wassup!");
        label.setBounds(0,0,100,100);
        label.setBackground(Color.red);
        label.setHorizontalTextPosition(JLabel.CENTER);
        label.setOpaque(true);

        this.add(label);
        this.setVisible(true);
        
    }

    @Override
    public void keyTyped(KeyEvent e) {
        switch(e.getKeyChar()) {
            case 'a':label.setLocation(label.getX()-10,label.getY());
            break;
            case 'w':label.setLocation(label.getX(),label.getY()-10);
            break;
            case 's':label.setLocation(label.getX(),label.getY()+10);
            break;
            case 'd':label.setLocation(label.getX()+10,label.getY());
            break;
        }
        
    }

    @Override
    public void keyPressed(KeyEvent e) {
        switch(e.getKeyCode()) {
            case 37:label.setLocation(label.getX()-10,label.getY());
            break;
            case 38:label.setLocation(label.getX(),label.getY()-10);
            break;
            case 40:label.setLocation(label.getX(),label.getY()+10);
            break;
            case 39:label.setLocation(label.getX()+10,label.getY());
            break;
        }
        
    }

    @Override
    public void keyReleased(KeyEvent e) {
        System.out.println("You released key character: " + e.getKeyChar());
        System.out.println("You released key code: " + e.getKeyCode());
        
    }
}
