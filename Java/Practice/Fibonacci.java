package Practice;
import javax.swing.JOptionPane;
public class Fibonacci {
    public static void main(String[] args){
       int num1 = 0, num2 = 1;
       String len = JOptionPane.showInputDialog("Enter how many digits of the Fibonacci sequence you want: ");
       int length = Integer.parseInt(len);
       for(int i = 1; i <= length; i++){
        System.out.print(num1 + " ");
        int num3 = num1 + num2;
        num1 = num2;
        num2 = num3;
       }
    }
}
