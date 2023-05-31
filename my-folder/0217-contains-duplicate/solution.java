class Solution {
    public boolean containsDuplicate(int[] nums) {
       Set<Integer> theSet = new HashSet<Integer>();
       for (int num : nums) {
           if (theSet.contains(num)) {
               return true;
           }
           theSet.add(num);
       }
       return false;
    }
}
