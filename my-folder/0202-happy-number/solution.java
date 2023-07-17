class Solution {
    public boolean isHappy(int n) {
        if (n == 1) {
            return true;
        } else if (n == 4) {
            return false;
        }
        
        int happy = 0;
        while (n > 0) {
            happy += (n % 10) * (n % 10);
            n /= 10;
        }
        
        return isHappy(happy);
    }
}

