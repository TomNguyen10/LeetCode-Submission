class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split(" ");
        int ans = arr[arr.length - 1].length();
        return ans;
    }
}
