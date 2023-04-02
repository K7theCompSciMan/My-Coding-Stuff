import java.io.FileWriter;
import java.io.IOException;

public class FileWriting {
    public static void main(String[] args) {
       
       try {
        FileWriter writer = new FileWriter("poem.txt");
        writer.write("Roses are red \nViolets are blue \nBlah Blah Blah \nI like you");
        writer.append("\n \n \n \n(A poem by K7)");
        writer.close();
       }
       catch (IOException e){
            e.printStackTrace();
       }
    }
}