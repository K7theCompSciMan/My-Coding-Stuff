package Practice;

import java.awt.Color;
import java.awt.event.*;
import javax.swing.*;

/**
 * PongGame
 */
public class PongGame {

    public static void main(String[] args) {
        new PongFrame("Pong Game");
    }
}

class PongFrame extends JFrame implements KeyListener {

    Player p1;
    Player p2;
    JPanel ball;
    JLabel l;
    
    PongFrame(String title){
        this.setTitle(title);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.setLayout(null);
        this.setSize(400,400);
        this.setBackground(Color.BLACK);
        this.addKeyListener(this);

        p1 = new Player(10,160);

        p2 = new Player(365,160);
        
        ball = new JPanel();

        l = new JLabel();
        l.setSize(400,400);
        l.setLayout(null);
        l.setBackground(Color.black);

        l.add(p1);
        l.add(p2);
        l.add(ball);
        this.add(l);
        this.setVisible(true);

    }

    @Override
    public void keyTyped(KeyEvent e) {       

    }

    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == 38) {
            if(p2.getY() > 10){
            p2.moveUp();
        }
        }
        if (e.getKeyCode() ==40) {
            if(p2.getY() < 400-p2.getHeight()){
                p2.moveDown();
            }
        }
        if (e.getKeyCode() == 87){
            if(p1.getY() > 10){
                p1.moveUp();
            }
        }
        if (e.getKeyCode() == 83){
            if(p1.getY() < 400-p1.getHeight()){
                p1.moveDown();
            }
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        
    }


}

class Player extends JPanel{
    Player(int x, int y){
        this.setBounds(x,y,10,80);
        this.setBackground(Color.WHITE);        
    }
    void moveUp(){
        this.setBounds(this.getBounds().x,this.getBounds().y-5,10,80);
    }
    void moveDown(){
        this.setBounds(this.getBounds().x,this.getBounds().y+5,10,80);
    }
}
