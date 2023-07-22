class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int maxScore=-1;
        int maxElement=-1;
        for(int i=0;i<divisors.length;i++){
            // count of numbers ith divisor can divide
            int score=0;
            for(int j=0;j<nums.length;j++){
                if(nums[j]%divisors[i]==0)
                    score++;
            }

            // updating max count
            if(score==maxScore) // edge condition
                maxElement=Math.min(maxElement,divisors[i]);
            else if(score>maxScore){
                maxScore=score;
                maxElement=divisors[i];
            }
        }
        return maxElement;
    }
}
