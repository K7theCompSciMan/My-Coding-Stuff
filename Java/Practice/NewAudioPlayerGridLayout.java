package Practice;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.Scanner;
import javax.sound.sampled.*;
import javax.swing.*;

public class NewAudioPlayerGridLayout {
    public static void main(String[] args) throws FileNotFoundException, UnsupportedAudioFileException, IOException, LineUnavailableException {
        new GridLayoutAudioFrame();
    }
}


class GridLayoutAudioFrame extends JFrame implements ActionListener{
    Scanner sc;

    JButton playpause;
    JButton loop;
    JButton stop;
    JButton reset;
    JButton quit;
    JButton forward;
    JButton backward;

    JPanel p = new JPanel();
    JPanel pc = new JPanel();
    JPanel pn = new JPanel();
    JPanel ps = new JPanel();
    JPanel pw = new JPanel();
    JPanel pe = new JPanel();

    ImageIcon forwardIcon;
    ImageIcon backwardIcon;
    ImageIcon playpauseIcon;
    ImageIcon stopIcon;
    ImageIcon quitIcon;
    ImageIcon replayIcon;
    ImageIcon loopIcon;
    JButton selectFile;

    File filepath;
    int loops;

    File file;
    AudioInputStream audioStream ;
    Clip clip;

    String response;

    ImageIcon icon;
    
    
    GridLayoutAudioFrame() throws UnsupportedAudioFileException, IOException, LineUnavailableException, FileNotFoundException{

        icon = new ImageIcon("IMG.jpg");

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        this.setSize(760,789);
        this.setTitle("Audio Player");
        this.setIconImage(icon.getImage());

        p = new JPanel();
        p.setLayout(new GridLayout(3,3,0,0));
        p.setBounds(0,0,750,750);

        // pc.setPreferredSize(new Dimension(250,250));
        // pn.setPreferredSize(new Dimension(500,250));
        // pw.setPreferredSize(new Dimension(250,500));
        // ps.setPreferredSize(new Dimension(500,250));
        // pe.setPreferredSize(new Dimension(250,500));


        selectFile = new JButton("Select File(.wav)");
        selectFile.setFocusable(false);
        selectFile.addActionListener(this);

        sc = new Scanner(System.in);
        while(true) {
            try {
                
                p.add(selectFile,BorderLayout.NORTH);
                this.add(p);
                this.setVisible(true);
                
                // System.out.println("Type 'done' once you have chosen a file.");
                // sc.next();
                
                // filePath = JOptionPane.showInputDialog("Enter your file's path (every backslash must be 2(two) backslashes or 1(one) forwardslash): ");
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                loops = Integer.parseInt(JOptionPane.showInputDialog("How many times do you want to loop?: "));

                this.setVisible(false);

                // file = new File(filePath); 

                audioStream = AudioSystem.getAudioInputStream(filepath);

                p.remove(selectFile);
                
                break;
            }
            catch(FileNotFoundException fne) {
                    System.out.println("That is not a valid path.");
            }
        }
        
        
        clip = AudioSystem.getClip();
        
        clip.open(audioStream);

        // icon = new ImageIcon("IMG.jpg");

        // this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // this.setSize(500,500);
        // this.setTitle("Audio Player");
        // this.setIconImage(icon.getImage());
        // JPanel p = new JPanel();

        forwardIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Fast Forward.jpg");
        backwardIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Backward.jpg");
        playpauseIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/playpause.png");
        stopIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Stop.png");
        quitIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Quit.png");
        replayIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Replay.png");
        loopIcon = new ImageIcon("C:/Users/tekid/Desktop/K7 Coding Stuff/Looppng.png");

        playpause = new button();
        playpause.setIcon(playpauseIcon);
        playpause.addActionListener(this);

        forward = new button();
        forward.setIcon(forwardIcon);
        forward.addActionListener(e -> clip.setMicrosecondPosition(clip.getMicrosecondPosition() + 5000000));

        backward = new button();
        backward.setIcon(backwardIcon);
        backward.addActionListener(e -> clip.setMicrosecondPosition(clip.getMicrosecondPosition() - 5000000));
	
	    loop = new button();
        loop.setIcon(loopIcon);
        loop.addActionListener(e -> clip.loop(loops));        


        reset = new button();
        reset.setIcon(replayIcon);
        reset.addActionListener(e -> clip.setMicrosecondPosition(0));

        quit = new button();
        quit.setIcon(quitIcon);
        quit.addActionListener(e -> clip.close());

        JButton empty1 = new JButton();
        JButton empty2 = new JButton();
        JButton empty3 = new JButton();

        // pn.setLayout(new FlowLayout(FlowLayout.CENTER));
        // pw.setLayout(new FlowLayout(FlowLayout.CENTER));
        // ps.setLayout(new FlowLayout(FlowLayout.CENTER));
        // pe.setLayout(new FlowLayout(FlowLayout.CENTER));

        // pn.add(forward);
        // pn.add(playpause);
        // pn.add(backward);
        // pw.add(loop);
        // pe.add(reset);
        // ps.add(quit);

        // p.add(pn,BorderLayout.NORTH);
        // p.add(pw,BorderLayout.WEST);
        // p.add(ps,BorderLayout.SOUTH);
        // p.add(pe,BorderLayout.EAST);

        p.add(loop);
        p.add(empty1);
        p.add(reset);
        p.add(backward);
        p.add(playpause);
        p.add(forward);
        p.add(empty2);
        p.add(quit);
        p.add(empty3);

        

        this.setVisible(true);
        // this.add(p);
        // this.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==selectFile) {

            JFileChooser fileChooser = new JFileChooser();

            fileChooser.setCurrentDirectory(new File("C:/Users/tekid/Desktop/Audio Player Audio(.wav)"));

            int response = fileChooser.showOpenDialog(null); //selects file to open 
            
            //int response = fileChooser.showSaveDialog(null); //selects file to save

            if(response ==JFileChooser.APPROVE_OPTION) {
              filepath = new File(fileChooser.getSelectedFile().getAbsolutePath());
            }
            
        }
        else if(e.getSource()==playpause) {
            if(clip.isRunning()) {
                clip.stop();
            }
            else {
                clip.start();
            }
        }
        
    }
}
class button extends JButton {
    button() {
        this.setFont(new Font("Comic Sans", Font.ITALIC, 25));
        this.setForeground(Color.ORANGE);
        this.setHorizontalTextPosition(JButton.CENTER);
        this.setFocusable(false);
        this.setPreferredSize(new Dimension(150,150));
        
    }
}
