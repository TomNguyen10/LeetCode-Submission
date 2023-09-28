class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        int[] freq = new int[10];
        for (int i = 0; i < nums1.length; i++) {
            freq[nums1[i]]++;
        }
        for (int i = 0; i < nums2.length; i++) {
            freq[nums2[i]]++;
        }

        int k = 2;
        int ans = 0;
        int mn1 = Arrays.stream(nums1).min().getAsInt();
        int mn2 = Arrays.stream(nums2).min().getAsInt();
        for (int i = 1; i <= 9; i++) {
            if (freq[i] == 2) {
                return i;
            }
        }

        if (mn2 < mn1) {
            int temp = mn2;
            mn2 = mn1;
            mn1 = temp;
        }
        return mn1 * 10 + mn2;
    }
}
