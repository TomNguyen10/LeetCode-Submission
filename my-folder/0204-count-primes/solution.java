class Solution {
    public int countPrimes(int n) {
        if (n < 2) {
            return 0;
        }
        
        boolean[] res = new boolean[n];
        Arrays.fill(res, true);
        res[0] = false;
        res[1] = false;
        for (int i = 2; i*i < n; i++) {
            if (res[i]) {
                for (int j = i*i; j < n; j += i) {
                    res[j] = false;
                 }
            }
        }

        int count = 0;
        for (boolean b : res) {
            if (b) count++;
        }

        return count;
    }
}
