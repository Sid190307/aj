
import java.util.*;

public class p2 {
    public static void main(String[] args) {

        Stack<String> st = new Stack<String>();

        st.push("AJ");
        st.push("For");
        st.push("Sy");
        st.push("students");

        Iterator<String> itr = st.iterator();

        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }

        System.out.println();

        st.pop();

        itr = st.iterator();

        while (itr.hasNext()) {
            System.out.print(itr.next() + " ");
        }
    }
}
