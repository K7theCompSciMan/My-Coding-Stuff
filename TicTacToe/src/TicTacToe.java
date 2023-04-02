import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class TicTacToe implements ActionListener {

    JFrame f = new JFrame();
    Random r = new Random();
    JPanel title_p = new JPanel();
    JPanel button_p = new JPanel();
    JLabel t = new JLabel();
    JButton[] buttons = new JButton[9];
    boolean p1_turn;

    TicTacToe(){

        //set up the frame
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(800,800);
        f.getContentPane().setBackground(new Color(0,0,0));
        f.setLayout(new BorderLayout());
        f.setVisible(true);

        //set up the label(textfield)
        t.setBackground(new Color(25,25,25));
        t.setForeground(new Color(25,255,0));
        t.setFont(new Font("Ink Free", Font.ITALIC,75));
        t.setHorizontalAlignment(JLabel.CENTER);
        t.setText("Tic-Tac-Toe");
        t.setOpaque(true);

        //set up the title panel
        title_p.setLayout(new BorderLayout());
        title_p.setBounds(0,0,800,100);
        title_p.add(t);

        //set up the button panel
        button_p.setLayout(new GridLayout(3,3));
        button_p.setBackground(new Color(150,150,150));

        for(int i=0;i<9;i++){
            buttons[i] = new JButton();
            button_p.add(buttons[i]);
            buttons[i].setFont(new Font("Verdana", Font.BOLD,120));
            buttons[i].setFocusable(false);
            buttons[i].addActionListener(this);
        }


        
        f.add(title_p, BorderLayout.NORTH);
        f.add(button_p);
        firstTurn();
    }
    
    
    
    @Override
    public void actionPerformed(ActionEvent e) {
        for(int i = 0;i<9;i++) {
            if(e.getSource()==buttons[i]) {
                if(p1_turn) {
                    if(buttons[i].getText()==""){
                        buttons[i].setForeground(Color.red);
                        buttons[i].setText("X");
                        p1_turn = false;
                        t.setText("O turn");
                        canWin();
                    }
                }
                else {
                    if(buttons[i].getText()=="") {
                        buttons[i].setForeground(Color.blue);
                        buttons[i].setText("O");
                        p1_turn = true;
                        t.setText("X turn");
                        canWin();
                    }
                }
            }
        }            
    }

    public void firstTurn(){

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        if(r.nextInt(2)==0){
            p1_turn = true;
            t.setText("X turn");
        }
        else {
            p1_turn = false;
            t.setText("O turn");
        }
    }

    public void canWin(){
        //check X matches
        if((buttons[0].getText()=="X") && (buttons[1].getText()=="X") && (buttons[2].getText()=="X")) {
            xWins(0,1,2);
        }
        else if((buttons[3].getText()=="X") && (buttons[4].getText()=="X") && (buttons[5].getText()=="X")) {
            xWins(3,4,5);
        }
        else if((buttons[6].getText()=="X") && (buttons[7].getText()=="X") && (buttons[8].getText()=="X")) {
            xWins(6,7,8);
        }
        else if((buttons[0].getText()=="X") && (buttons[3].getText()=="X") && (buttons[6].getText()=="X")) {
            xWins(0,3,6);
        }
        else if((buttons[1].getText()=="X") && (buttons[4].getText()=="X") && (buttons[7].getText()=="X")) {
            xWins(1,4,7);
        }
        else if((buttons[2].getText()=="X") && (buttons[5].getText()=="X") && (buttons[8].getText()=="X")) {
            xWins(2,5,8);
        }
        else if((buttons[0].getText()=="X") && (buttons[4].getText()=="X") && (buttons[8].getText()=="X")) {
            xWins(0,4,8);
        }
        else if((buttons[2].getText()=="X") && (buttons[4].getText()=="X") && (buttons[6].getText()=="X")) {
            xWins(2,4,6);
        }


        //check O matches
        if((buttons[0].getText()=="O") && (buttons[1].getText()=="O") && (buttons[2].getText()=="O")) {
            oWins(0,1,2);
        }
        else if((buttons[3].getText()=="O") && (buttons[4].getText()=="O") && (buttons[5].getText()=="O")) {
            oWins(3,4,5);
        }
        else if((buttons[6].getText()=="O") && (buttons[7].getText()=="O") && (buttons[8].getText()=="O")) {
            oWins(6,7,8);
        }
        else if((buttons[0].getText()=="O") && (buttons[3].getText()=="O") && (buttons[6].getText()=="O")) {
            oWins(0,3,6);
        }
        else if((buttons[1].getText()=="O") && (buttons[4].getText()=="O") && (buttons[7].getText()=="O")) {
            oWins(1,4,7);
        }
        else if((buttons[2].getText()=="O") && (buttons[5].getText()=="O") && (buttons[8].getText()=="O")) {
            oWins(2,5,8);
        }
        else if((buttons[0].getText()=="O") && (buttons[4].getText()=="O") && (buttons[8].getText()=="O")) {
            oWins(0,4,8);
        }
        else if((buttons[2].getText()=="O") && (buttons[4].getText()=="O") && (buttons[6].getText()=="O")) {
            oWins(2,4,6);
        }


    }

    public void xWins(int a, int b, int c){

        buttons[a].setBackground(Color.green);
        buttons[b].setBackground(Color.green);
        buttons[c].setBackground(Color.green);

        for(int i = 0; i < 9; i ++){
            buttons[i].setEnabled(false);
        }
        t.setText("X wins");

    }

    public void oWins(int a, int b, int c){

        buttons[a].setBackground(Color.green);
        buttons[b].setBackground(Color.green);
        buttons[c].setBackground(Color.green);

        for(int i = 0; i < 9; i ++){
            buttons[i].setEnabled(false);
        }
        t.setText("O wins");

    }

    
}
