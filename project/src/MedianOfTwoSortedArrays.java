class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
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
    public double oN(int[] nums1, int[] nums2) {
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