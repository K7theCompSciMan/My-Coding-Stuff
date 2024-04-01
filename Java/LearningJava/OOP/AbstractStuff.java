package OOP;

public class AbstractStuff {
    public static void main(String[] args) {
        ABCar car = new ABCar();
        //ABVehicle vehicle = new ABVehicle();
        car.go();
    }
}
abstract class ABVehicle{
    
    abstract void go();
}
class ABCar extends ABVehicle{
    
    void go(){
        System.out.println("The driver is driving the car.");
    }
}