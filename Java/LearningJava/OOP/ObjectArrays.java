package OOP;

public class ObjectArrays {
    public static void main(String[] args) {
        //ObjectArraysFood[] refrigerator = new ObjectArraysFood[5];

        ObjectArraysFood food1 = new ObjectArraysFood("Pizza");
        ObjectArraysFood food2 = new ObjectArraysFood("Hamburger");
        ObjectArraysFood food3 = new ObjectArraysFood("Burger");
        ObjectArraysFood food4 = new ObjectArraysFood("Hotdog");
        ObjectArraysFood food5 = new ObjectArraysFood("Puri");

        ObjectArraysFood[] refrigerator = {food1, food2, food3, food4, food5};

        //refrigerator[0] = food1;
        //refrigerator[1] = food2;
        //refrigerator[2] = food3;
        //refrigerator[3] = food4;
        //refrigerator[4] = food5;

        System.out.println(refrigerator[0].name);
        System.out.println(refrigerator[1].name);
        System.out.println(refrigerator[2].name);
        System.out.println(refrigerator[3].name);
        System.out.println(refrigerator[4].name);
    }
}
class ObjectArraysFood {
    String name;
    ObjectArraysFood(String name){
        this.name = name;
    }
}