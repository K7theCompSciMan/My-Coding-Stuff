package OOP;

public class Inheritance {
    public static void main(String[] args) {
        InCar car = new InCar();
        car.go();
        Bycicle bike = new Bycicle();
        bike.stop();
        System.out.println(car.doors);
        System.out.println(bike.pedals);
    }
}
class InCar extends Vehicle {
    int wheels = 4;
    int doors = 4;
}
class Bycicle extends Vehicle {
    int wheels = 2;
    int pedals = 2;
}
class Vehicle{
    double speed;

    void go() {
        System.out.println("This vehicle is moving.");
    }
    void stop() {
        System.out.println("This vehicle is stopped.");
    }
}