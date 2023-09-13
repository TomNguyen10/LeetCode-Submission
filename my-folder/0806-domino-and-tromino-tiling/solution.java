class Solution {
    public int numTilings(int N) {
        int MOD = 1000000007;
        long[] v = new long[1001];
        v[1] = 1;
        v[2] = 2;
        v[3] = 5;

        if (N <= 3) return (int) v[N];

        for (int i = 4; i <= N; i++) {
            v[i] = 2 * v[i - 1] + v[i - 3];
            v[i] %= MOD;
        }

        return (int) v[N];
    }
}
