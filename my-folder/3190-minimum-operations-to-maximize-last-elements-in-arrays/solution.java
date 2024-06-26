class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int a = nums1[n-1];
        int b = nums2[n-1];

        int swap1 = 0;
        int flag1 = 1;

        for(int i=0;i<n-1;i++){
            if(nums1[i]<=a && nums2[i]<=b)
                continue;
            else if(nums2[i]<=a && nums1[i]<=b)
                swap1++;
            else{
                flag1 = 0;
                break;
            }
        }

        int swap2 = 1;
        int flag2 = 1;
        for(int i=0;i<n-1;i++){
            if(nums1[i]<=b && nums2[i]<=a)
                continue;
            else if(nums2[i]<=b && nums1[i]<=a)
                swap2++;
            else{
                flag2 = 0;
                break;
            }
        }
        if(flag1==0 && flag2==0)
            return -1;
        return Math.min(swap1,swap2);
    }
}

