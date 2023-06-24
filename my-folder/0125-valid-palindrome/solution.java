class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            char head = s.charAt(i);
            char tail = s.charAt(j);

            if (!Character.isLetterOrDigit(head)) {
                i++;
                continue;
            }

            if (!Character.isLetterOrDigit(tail)) {
                j--;
                continue;
            }

            if (Character.toLowerCase(head) != Character.toLowerCase(tail)) return false;
        
            i++;
            j--;
        
        }

        return true;
    }
}
