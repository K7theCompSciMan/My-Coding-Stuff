import java.util.Scanner;
public class iffs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your age: ");
        double age = scanner.nextDouble();
        
        if (age>=75) {
            System.out.println("Ok Boomer!");
        }
        else if(age>=18){
            System.out.println("You are an adult. ");
        }
        else if(age>=13){
            System.out.println("You are a teenager. ");
        }
        else {
            System.out.println("You are not an adult.");
        }
        scanner.close();
    }
}
