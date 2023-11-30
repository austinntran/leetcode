import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongSubstring {
    public static void main(String args[]) {
        System.out.println(lengthOfLongestSubstring("tmmzuxt"));
    }

    public static int lengthOfLongestSubstring(String s) {
        int run = 0;
        int start = 0;
        Map<Character, Integer> pointer = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Integer prev = pointer.put(s.charAt(i), i);
            if (prev == null || prev < start) {
                run = Math.max(run, i - start + 1);
            }
            else {
                start = prev + 1;
            }
        }
        return run;
    }
}
