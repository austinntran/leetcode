class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        return oLogMPlusN(nums1, nums2);
    }
    public static double oLogMPlusN(int[] nums1, int[] nums2) {
        // Ensure nums2 is always larger or equal to the length of nums1
        int length1 = nums1.length;
        int length2 = nums2.length;
        if (length1 > length2) {
            return oLogMPlusN(nums2, nums1);
        }
        boolean even = (length1 + length2) % 2 == 0;
        int bottom = 0, top = length1;
        // Create index range for num1 where {nums1[0:midpoint], nums2[0:partitionSize2]} contains the numbers before the median
        // {nums1[midpoint:end], nums2[partitionSize2:end]} contains all numbers after the median
        while (bottom <= top) {
            int midpoint1 = (bottom + top) / 2;
            int partitionSize2 = (length1 + length2) / 2 - midpoint1;
            // Get the largest value in nums1 on the left partition
            int maxLeft1 = midpoint1 == 0? Integer.MIN_VALUE: nums1[midpoint1 - 1];
            // Get the smallest value in nums1 on the right side partition
            int minRight1 = midpoint1 == length1? Integer.MAX_VALUE: nums1[midpoint1];
            // Get the largest value in nums2 on the left partition
            int maxLeft2 = partitionSize2 == 0? Integer.MIN_VALUE: nums2[partitionSize2 - 1];
            // Get the smallest value in nums2 on the right partition
            int minRight2 = partitionSize2 == length2? Integer.MAX_VALUE:nums2[partitionSize2];
            
            // If the largest value on the left partition is less than the smallest value of the right partition of the opposing arrays
            // The midpoint and partitions split the arrays in two halves that each make up the numbers on either side of the partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Calculate the median for even and odd numbers
                return even? (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0: Math.min(minRight1, minRight2);
            }

            // If the left partition of nums1 contains too big of numbers, make the partition halve itself to its smaller half
            if (maxLeft1 > minRight2) {
                top = midpoint1 - 1;
            }
            else {
                // If the left partition of nums2 contains too big of numbers, make the nums1 left partition halve itself to its larger half
                bottom = midpoint1 + 1;
            }
        }
        return 0;
    }
    public static double oMPlusN(int[] nums1, int[] nums2) {
        int totalLength = nums1.length + nums2.length;
        int medianSlot = totalLength / 2;
        int sorted[] = new int[totalLength];
        int pointer1 = 0;
        int pointer2 = 0;
        for (int i = 0; i < medianSlot + 1; i++) {
            if (pointer1 == nums1.length) {
                sorted[i] = nums2[pointer2];
                pointer2++;
            }
            else if (pointer2 == nums2.length) {
                sorted[i] = nums1[pointer1];
                pointer1++;
            }
            else if (nums1[pointer1] < nums2[pointer2]) {
                sorted[i] = nums1[pointer1];
                pointer1++;
            }
            else {
                sorted[i] = nums2[pointer2];
                pointer2++;
            }
        }
        if (totalLength % 2 == 0) {
            return (sorted[medianSlot - 1] + sorted[medianSlot]) / 2.0;
        }

        return sorted[medianSlot];
    }
    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[] {1, 3}, new int[]{2}));
    }
}