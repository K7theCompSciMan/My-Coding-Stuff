public class Arrays {
    public static void main(String[] args){
        String[] cars = {"Camaro", "Corvette", "Tesla", "BMW"}; //Has to be all 1 type. All Strings in this case.
        cars[0] = "Mustang";
        System.out.println(cars[3]);

        String[] newcars = new String[3];

        newcars[0] = "Camaro";
        newcars[1] = "Corvette";
        newcars[2] = "Tesla";
        System.out.println(newcars[2]);

        for(int i = 0; i<newcars.length; i++){
            System.out.println(newcars[i]);
        }
    //Arrays are like Lists in python.
    }
}