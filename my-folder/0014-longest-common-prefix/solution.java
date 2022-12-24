class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        int min = strs[0].length();
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].length() < min) {
                min = strs[i].length();
            }
        }
        int left = 1;
        int right = min;
        while (left <= right) {
            int mid = (left + right)/2;
            if (isCommon(strs, mid)) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return strs[0].substring(0, (left + right)/2);
    }

    private boolean isCommon (String[] strs, int len) {
        String str = strs[0].substring(0, len);
        for (int i = 1; i < strs.length; i++) {
            if (!strs[i].startsWith(str)) {
                return false;
            }
        }
        return true;
    } 
}
