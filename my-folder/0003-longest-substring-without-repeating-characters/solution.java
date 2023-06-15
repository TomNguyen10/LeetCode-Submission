class Solution {

    public int lengthOfLongestSubstring(String s) {
        List<Character> list = new ArrayList<>();
        int max = 0;

        for(int i = 0; i < s.length(); i++) {

            if(list.contains(s.charAt(i))) { 
                int index = list.indexOf(s.charAt(i));
                list.remove(index);
                if(index > 0) {
                    list.subList(0, index).clear();
                }
            }
            list.add(s.charAt(i));
            max = Math.max(max, list.size());
        }
        return max;
    }
}

