class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<>();
        while (left <= right) {
            if (isDivided(left)) {
                res.add(left);
            }
            left++;
        }
        return res;
    }

    private boolean isDivided(int num) {
        for (int n = num; n > 0; n /= 10) {
            if (n % 10 == 0 || num % (n % 10) != 0) return false;
        }
        return true;
    }
}
