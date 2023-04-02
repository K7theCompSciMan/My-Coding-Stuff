package Practice;

import java.util.Scanner;

public class CommaAdder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number: ");
        String number = scanner.nextLine();
        number = addCommas(number);
        System.out.println(number);
        scanner.close();
    }
    public static String addCommas(String number) {
        StringBuffer stringBuffer = new StringBuffer(number);
        
        int count = 1;
        for(int i = 0; i < number.length(); i++) {
            if(i+count == number.length()){
                break;
            }
            if ((i+count) %3 == 0) {
                stringBuffer.insert(number.length()-i-count, ",");
                count++;
            }
        }
        
        return stringBuffer.toString();
    }
}
