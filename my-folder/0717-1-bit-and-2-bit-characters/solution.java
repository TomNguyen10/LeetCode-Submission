class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int ones = 0;
        for (int i = bits.length - 2; i >= 0 && bits[i] == 1;i--) { 
            ones++;
        }
        if (ones % 2 > 0) 
            return false; 
        return true;
    }
}
