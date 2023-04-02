public class MethodsStuff {
    public static void main(String[] args){
        String name = "K7";
        int age = 21;
        hello(name, age);

        int x = 3;
        int y = 4;
        //int z = add(x,y);
        //System.out.println(z);
        // or
        System.out.println(add(x,y));
        
    }

    static void hello(String name, int age){
        System.out.println("Hello! " + name);
        System.out.println("You are " + age + " years old");
    }
    static int add(int x, int y){        
        return x + y;
    }
    
}
