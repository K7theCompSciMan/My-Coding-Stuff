package OOP;

public class Constructors {
    public static void main(String[] args) {
        HumanConstructors human1 = new HumanConstructors("Rick", 65, 70);
        HumanConstructors human2 = new HumanConstructors("Morty", 16, 50);
        System.out.println(human1.name);
        System.out.println(human2.name);
        human2.eat();
        human1.drink();
    }    
    
    
}
class HumanConstructors {
    String name;
    int age;
    double weightInKg;

    HumanConstructors(String name, int age, double weightInKg){
        
        this.name = name;
        this.age = age;
        this.weightInKg = weightInKg;
    }
    void eat(){
        System.out.println(this.name + " is eating.");
    }
    void drink(){
        System.out.println(this.name + " is drinking.");
    }
}