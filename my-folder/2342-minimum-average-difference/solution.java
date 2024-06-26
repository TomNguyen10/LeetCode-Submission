class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n=nums.length;
        //if length==1 difference=0
        if(n==1)return 0;
        // initialsing left and right sum
        long right=0,left=0;
        //ans will contain index
        int ans=0;
        //mina will contain minimum difference found till now
        long mina=100001;
        for(Integer i:nums){right+=i;}//right=total sum

        //iterating on array and obtaining corresponding difference
        for(int i=0; i<n; i++){

            //left sum increases on each iteration
            left+=nums[i];
            //right sum decreases on each iteration
            right-=nums[i];
            //avl -> average of left side
            long avl=left/(i+1);
            //avr-> average of right side
            long avr=0;
            //for last index right=0 , avr=0
            if(i!=n-1){avr=right/(n-1-i);}

            //if current difference is less than mina 
            if(Math.abs(avl-avr)<mina)
            {
                //update mina 
            mina=Math.abs(avl-avr);
            //update ans index
            ans=i;}
        }
        // return ans index
        return ans;
    }
}
//Thank you
//Upvote if found helpful.
