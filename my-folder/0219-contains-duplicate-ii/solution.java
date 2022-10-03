class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
	
	    for(int i = 0; i <  nums.length; i++) {
		    Integer z = map.put(nums[i], i);
		    if(z != null && i - z <= k) {
			    return true;
		    }
	    }
	    return false;
    }
}
