import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static void main(String[] args) {
        Arrays.stream(twoSum(new int[]{1, 2, 3}, 3)).forEach(System.out::println);
    }
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> compliments = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            if (compliments.containsKey(current)) {
                return new int[]{i, compliments.get(current)};
            }
            compliments.put(target - current, i);
        }
        return new int[0];
    }
}
