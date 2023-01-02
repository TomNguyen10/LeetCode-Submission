class Solution {
    public int[] plusOne(int[] digits) {
        int last = digits.length - 1;
        digits[last] += 1;
        for (int i = last; i > 0; i--) {
            if (digits[i] > 9) {
                digits[i] -= 10;
                digits[i-1] += 1; 
            }
        }
        int[] res = digits;
        if (digits[0] >= 10) {
            digits = new int[last+2];
            digits[0] = 1;
            digits[1] = res[0] - 10;
            for (int i = 1; i < res.length; i++) {
                digits[i+1] = res[i];
            }
            return digits;
        }
        return res;
    }
}
