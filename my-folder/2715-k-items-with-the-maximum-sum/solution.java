class Solution {
    public int kItemsWithMaximumSum(int ones, int zeros, int negones, int k) {
        if (k <= ones) return k;
        else if (k <= ones + zeros) return ones;
        return ones + (k - ones - zeros) * (-1);
    }
}
