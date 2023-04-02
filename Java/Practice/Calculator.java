package Practice;
import java.util.Scanner;
public class Calculator {
    public static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){
        double num1 = inp1(); 
        double num2 = inp2();
        while(true){
            System.out.println("Enter your option. \n     1. Addition \n     2. Subtraction \n     3. Multiplication \n     4. Division ");
            String opt = scanner.next();
            if(opt.equals("1")){
                System.out.println("Your solution is: " + add(num1,num2));
                break;
            }
            else if(opt.equals("2")){
                System.out.println("Your solution is: " + subtract(num1,num2));
                break;
            }
            else if(opt.equals("3")){
                System.out.println("Your solution is: " + mult(num1,num2));
                break;
            }
            else if(opt.equals("4")){
                System.out.println("Your solution is: " + div(num1,num2));
                break;
            }
            else 
            {
                System.out.println("Invalid entry. Try again");
            }
        }
        scanner.close();
    }

    static double add(double x, double y){
        return x + y;
    }

    static double subtract(double x, double y){
        return x - y;
    }

    static double mult(double x, double y){
        return x * y;
    }

    static double div(double x, double y){
        return x / y;
    }

    static boolean isNumeric(String strNum) {
        if (strNum == null){
            return false;
        }
        try {
            Double d = Double.parseDouble(strNum);
            d.doubleValue();
        }
        catch (NumberFormatException nfe){
            return false;
        }
        return true;
        
    }

    static double inp1(){
        
        double num1;
        while(true){
            System.out.println("Enter your first number: ");
            String num1s = scanner.nextLine();
            if (isNumeric(num1s) == true) {
              num1 = Double.parseDouble(num1s);
              break;
            }
            else {
                System.out.println("Invalid entry. Try again!");
            }
        }
        return num1;
    }

    static double inp2(){
        double num2;
        while(true){
            System.out.println("Enter your second number: ");
            String num2s = scanner.nextLine();
            if (isNumeric(num2s) == true) {
              num2 = Double.parseDouble(num2s);
              break;
            }
            else {
                System.out.println("Invalid entry. Try again!");
            }
        }
        return num2;
    }
}