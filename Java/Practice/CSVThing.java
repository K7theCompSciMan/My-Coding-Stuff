package Practice;

import java.io.*;  
import java.util.Scanner;  
public class CSVThing   
{  
public static void main(String[] args) throws Exception  
{  

Scanner sc = new Scanner(new File("CSVDemo.csv"));

sc.useDelimiter(",");    

while (sc.hasNext()) {  
    System.out.print(sc.next());  
    System.out.print(" ");
}   
sc.close(); 
}  
}  