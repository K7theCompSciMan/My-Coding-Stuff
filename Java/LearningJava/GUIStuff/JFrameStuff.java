
public class JFrameStuff {
    public static void main(String[] args) {
        /* 
        JFrame frame = new JFrame(); //creates a frame

        frame.setTitle("JFrame title goes here"); //sets the title of frame

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //exit out of application

        frame.setResizable(false); //doesn't allow resizing

        frame.setSize(420,420); //sets (x,y) dimension of frame

        frame.setVisible(true); //makes frame visible

        ImageIcon image = new ImageIcon("IMG.jpg"); //creates an image icon

        frame.setIconImage(image.getImage()); //sets icon to image

        frame.getContentPane().setBackground(new Color(123,50,250));  //changes bg color ****Good Color
        */

        MyFrame myFrame = new MyFrame();
        myFrame.setTitle("myFrame Title");
    }
}