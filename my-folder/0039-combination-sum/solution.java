class Solution {
    HashSet<List<Integer>> set = new HashSet<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> tempList = new ArrayList<>();
        backtrack(tempList,candidates,target,0);
        List<List<Integer>> read = new ArrayList<>();
        for(List<Integer> ls:set){
            read.add(ls);
        }
        return read;
    }
    
    public void backtrack(List<Integer> tempList,int[] candidates,int target,int start){
        if(target==0){
            set.add(new ArrayList<>(tempList));
            return;
        }
        for(int i=start;i<candidates.length;i++){
            if(candidates[i]>target) 
                continue;
            tempList.add(candidates[i]);
            backtrack(tempList,candidates,target-candidates[i],i);
            tempList.remove(tempList.size()-1);
        }
    }
}
