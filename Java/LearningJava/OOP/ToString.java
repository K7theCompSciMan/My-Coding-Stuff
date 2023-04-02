package OOP;

public class ToString {
    public static void main(String[] args) {
        ToStringCar car = new ToStringCar();
        //System.out.println(car);
        System.out.println(car.toString());
    }
}
class ToStringCar {
    String make = "Ford";
    String model = "F-150";
    String color = "black";
    int year = 2022;

    public String toString(){
        return make + "\n" + model + "\n" + color + "\n" + year;
    }
}

