package OOP;

public class ObjectPassing {
    public static void main(String[] args) {
        OPGarage garage = new OPGarage();

        OPCar car1 = new OPCar("BMW");
        OPCar car2 = new OPCar("Tesla");
        
        garage.park(car1);
        garage.park(car2);
    }
}
class OPCar {
    String name;
    
    OPCar(String name) {
        this.name = name;
    }
}
class OPGarage {
    void park(OPCar car){
        System.out.println("The " + car.name + " is parked in the garage.");
    }
}
