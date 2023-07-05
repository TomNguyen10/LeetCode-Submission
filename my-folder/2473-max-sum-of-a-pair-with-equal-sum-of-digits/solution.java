class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int max = -1;

        for (int num : nums) {
            int digit = calculate(num);
            if (map.containsKey(digit)) {
                int cur = map.get(digit);
                max = Math.max(max, cur + num);
                map.put(digit, Math.max(cur, num));
            }
            else {
                map.put(digit, num);
            }
        }

        return max;
    }

    private int calculate(int n) {
        int sum = 0;

        while (n > 0) {
            int rem = n % 10;
            sum += rem;
            n /= 10;
        }

        return sum;
    }
}
