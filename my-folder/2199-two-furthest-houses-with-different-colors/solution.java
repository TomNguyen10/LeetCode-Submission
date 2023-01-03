class Solution {
    public int maxDistance(int[] colors) {
        int i = 0; 
        int len = colors.length;
        int j = len - 1;
        while (colors[j] == colors[0]) {
            --j;
        }
        while (colors[i] == colors[len-1]) {
            ++i;
        }
        return Math.max(j, len-1-i);
    }
}
