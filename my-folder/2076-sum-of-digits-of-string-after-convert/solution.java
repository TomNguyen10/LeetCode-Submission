class Solution {
    public int getLucky(String s, int k) {
        int[] lettersTransformedOnce  = new int[26];
        for(int i = 0; i< 26;i++ ){
            int curLetterNum = i +1;
            while(curLetterNum > 0) {
                lettersTransformedOnce[i] += curLetterNum%10; 
                curLetterNum /= 10;
            }
        }
        int result = 0;
        for(int i = 0 ; i < s.length() ; i++ ) {
            int letterIdx = s.charAt(i) - 'a';
            result += lettersTransformedOnce[letterIdx]; 
        }
        for(int i=1;i<k;i++ ) {
            int temp = result;
            result =0;
            while(temp>0) {
                result += temp% 10;
                temp/=10;
            }
        }
        return result;
    }
}
