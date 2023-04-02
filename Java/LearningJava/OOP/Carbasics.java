package OOP;

public class Carbasics {
    public static void main(String[] args) {
        Car car1 = new Car();
        //System.out.println(car1.color);
        //System.out.println(car1.make);
        //System.out.println(car1.model);
        //myCar.drive();
        car1.brake();

        Car car2 = new Car();

        System.out.println(car2.make);
        System.out.println(car2.model);
        System.out.println("My car costs $" + car2.price);        
    }
}
class Car {
    String make = "Chevrolet";
    String model = "Corvette";
    int year = 2020;
    String color = "Blue";
    double price = 50000.00;

    void drive(){
        System.out.println("You drive the car.");
    }
    void brake(){
        System.out.println("You step on the brakes.");
    }
}

