class Solution {
    public int candy(int[] ratings) {
        int[] candy = new int[ratings.length];
        Arrays.fill(candy, 1);
        for (int i = 1; i < candy.length; i++) {
            if (ratings[i] > ratings[i-1]) {
                candy[i] = candy[i-1] + 1;
            }
        }
        for (int i = candy.length - 1; i > 0; i--) {
            if (ratings[i-1] > ratings[i]) {
                candy[i-1] = Math.max(candy[i]+1, candy[i-1]);
            }
        }
        int res = 0;
        for (int i : candy) {
            res += i;
        }
        return res;
    }
}
