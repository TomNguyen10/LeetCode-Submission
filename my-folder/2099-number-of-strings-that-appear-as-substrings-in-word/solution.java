class Solution {
    public int numOfStrings(String[] patterns, String word) {
        if (patterns.length == 0 || word == null) 
            return 0;
        
        int count = 0; 
        for (int i = 0; i < patterns.length; i++) {
            String sub = patterns[i];
            if (word.indexOf(sub) != -1) 
                count++;
        }

        return count;
    }
}
