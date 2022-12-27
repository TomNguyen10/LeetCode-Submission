class Solution {
    public int divisorSubstrings(int num, int k) {
        int count = 0;
        String s = Integer.toString(num);
        int i = 0;
        int j = k; 
        while (j <= s.length()) {
            String sub = s.substring(i,j);
            Integer cons = Integer.valueOf(sub);
            if (cons != 0) {
                if (num % cons == 0) 
                    count++;
            }
            i++;
            j++;
        }
        return count;
    }
}
