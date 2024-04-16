class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            char c1 = s.charAt(left);
            char c2 = s.charAt(right);
            if (!Character.isLetterOrDigit(c1)) {
                left++;
            }
            else if (!Character.isLetterOrDigit(c2)) {
                right--;
            }
            else if (Character.toLowerCase(c1) != Character.toLowerCase(c2)) {
                return false;
            }
            else {
                left++;
                right--;
            }
            System.out.println(c1);
            System.out.println(c2);
            System.out.println(c1 == c2);
        }
        return true;
    }
}
