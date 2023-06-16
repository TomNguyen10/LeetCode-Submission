class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int len = s1.length();
        int left = 0;
        int right = left + s1.length() - 1;

        char[] arr1 = s1.toCharArray();
        Arrays.sort(arr1);
        String val1 = String.valueOf(arr1);

        while (right < s2.length()) {
            String sub = s2.substring(left, right+1);
            char[] arr2 = sub.toCharArray();
            Arrays.sort(arr2);
            String val2 = String.valueOf(arr2);

            if (val1.equals(val2)) return true;
            left++;
            right++;
        }

        return false;
    }
}
