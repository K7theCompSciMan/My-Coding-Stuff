package Practice;

import java.util.Scanner;

public class PalindromeDetector {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a word: ");
        String word = scanner.nextLine().toLowerCase();
        System.out.println(isPalindrome(word));  
        scanner.close();      
    }
    public static String isPalindrome(String word) {
        int count = 0;
        for(int i =0; i < word.length(); i++) {
            if (word.charAt(i) == word.charAt(word.length()-1-i))
            {
                count++;
            }
        }
        if( count == word.length()){
            return "That word is a palindrome";
        }
        return "That word is not a palindrome";
    }
}
