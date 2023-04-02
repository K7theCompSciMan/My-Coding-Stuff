package OOP;

public class Overriding {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Dog dog = new Dog();
        dog.speak();
        animal.speak();
    }
}
class Animal {
    void speak(){
        System.out.println("The animal speaks.");
    }
}
class Dog extends Animal {
    //@override
    void speak(){
        System.out.println("The dog goes *bark*.");
    }
}