class Solution {
    public int reverse(int x) {
        int rep = Math.abs(x);
        int res = 0;
        while (rep > 0) {
            if (res > (Integer.MAX_VALUE - rep % 10) / 10) {
                return 0;
            }
            res = res * 10 + rep % 10;
            rep /= 10;
        }
        return x < 0 ? -res : res;
    }
}

