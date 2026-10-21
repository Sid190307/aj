
import java.util.*;

public class p3 {
    public static void main(String[] args) {

        HashMap<String, Integer> h = new HashMap<String, Integer>();

        h.put("Cat", 10);
        h.put("Dog", 20);
        h.put("Lion", 30);
        h.put("Tiger", 40);

        System.out.println("Map = " + h);

        System.out.println("Value of lion: " + h.get("Lion"));

        System.out.println("Size of the Map: " + h.size());

        System.out.println("Map Contains Key Lion: " + h.containsKey("Lion"));

        System.out.println("Map contains Value 20: " + h.containsValue(20));

        System.out.println("Map Empty: " + h.isEmpty());

        h.remove("Lion");
        System.out.println("Map after removing lion: " + h);

        h.replace("Cat", 50);
        System.out.println("Value of cat after replacing it: " + h);

        h.clear();
        System.out.println("Map after clearing: " + h);
    }
}
