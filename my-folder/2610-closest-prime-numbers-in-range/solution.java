class Solution {
    public int[] closestPrimes(int left, int right) {
        List<Integer> pl = list(left, right);
        int min = right;
        int[] res = new int[]{-1, -1};
        if (pl.size() < 2) return res;
        for (int i = 1; i < pl.size(); i++) {
            if (pl.get(i) - pl.get(i-1) < min) {
                res[0] = pl.get(i-1);
                res[1] = pl.get(i);
                min = pl.get(i) - pl.get(i-1);
            }
        }
        return res;
    }

    public List<Integer> list(int left, int right) {
        List<Integer> res = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            if(isPrime(i)) res.add(i);
        }
        return res;
    }

    public boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i*i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
