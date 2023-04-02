
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

public class StuffWithJOptionPane {
    public static void main(String[] args) {
        //JOptionPane.showMessageDialog(null,"This is some useless stuff.", "Title", JOptionPane.PLAIN_MESSAGE);
        //JOptionPane.showMessageDialog(null,"This is some useless stuff.", "Title", JOptionPane.INFORMATION_MESSAGE); // has 'i' icon
        //JOptionPane.showMessageDialog(null,"WHAT?", "Title", JOptionPane.QUESTION_MESSAGE); // has 'Q' icon
        //JOptionPane.showMessageDialog(null,"YOUR COMPUTER HAS VIRUS, BETA *in Indian Accent*.", "Title", JOptionPane.WARNING_MESSAGE); // has hazard icon
        //JOptionPane.showMessageDialog(null,"Some error occured.", "Title", JOptionPane.ERROR_MESSAGE); // has error icon
        //int answer = (JOptionPane.showConfirmDialog(null, "Bro, DO YOU EVEN CODE???", "THIS IS MY TITLE", JOptionPane.YES_NO_CANCEL_OPTION));// you can have different responses
        //String name = JOptionPane.showInputDialog(null, "What is your name?: ");
        //System.out.println("Hello " + name);
        
        String[] responses = {"No, you're awesome!", "Thank You.", "*blush"};

        ImageIcon icon = new ImageIcon("IMG.jpg");

        JOptionPane.showInternalOptionDialog(
            null,
            "You are awesome",
            "Secret Message", 
            JOptionPane.YES_NO_CANCEL_OPTION, 
            JOptionPane.INFORMATION_MESSAGE, 
            icon,
            responses, 
            0);
    }
}
