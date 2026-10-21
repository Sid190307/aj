
import java.util.*;

public class p3 {
    public static void main(String[] args) {

        HashSet<String> h = new HashSet<String>();

        h.add("Cat");
        h.add("Dog");
        h.add("Lion");

        System.out.println("Set = " + h);

        System.out.println("Size of the Set: " + h.size());

        System.out.println("Set Contains Lion: " + h.contains("Lion"));

        System.out.println("Set Empty: " + h.isEmpty());

        h.remove("Lion");
        System.out.println("Set after removing lion: " + h);

        h.clear();
        System.out.println("Set after clearing: " + h);
    }
}
