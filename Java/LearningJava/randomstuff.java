import java.util.Random;
public class randomstuff {
    public static void main(String[] args) {
        Random random = new Random();
        
        int x = random.nextInt(7);
        double y = random.nextDouble();
        boolean z = random.nextBoolean();

        System.out.println(x);
        System.out.println(z);
        System.out.println(y);
    }
}
