class Solution {
    public boolean buddyStrings(String s, String goal) {
        
        List<Integer> arrList = new ArrayList<>();

        // if (s.length() == 2){
        //     if (s.charAt(0) == s.charAt(1) && s.equals(goal)) return true;
        // } 
        // else{
        //     if (s.equals(goal)) return false;
        // }
        if (s.length() != goal.length()) return false;
        if (s.equals(goal)){
            Set<Character> set = new HashSet<Character>();
            for (char c : s.toCharArray()) set.add(c);
            return set.size() < s.length();
        }
        
        //har c;
        for (int i = 0; i< s.length(); i++){
           if (goal.charAt(i) != s.charAt(i)){
                arrList.add(i);
                //map.put(goal.charAt(i), i);
                //c = goal.charAt(i);
            }
        }
        if (arrList.size() != 2 ){
            return false;
        }
        else{
            int index1 = arrList.get(0);
            int index2 = arrList.get(1);
            if (goal.charAt(index1) == s.charAt(index2) && 
                goal.charAt(index2) == s.charAt(index1)){
                    return true;
                }
        }
        return false;
    }
}
