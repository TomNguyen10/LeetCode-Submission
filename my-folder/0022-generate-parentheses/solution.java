class Solution {
    public ArrayList<String> generateParenthesis(int n) {
        ArrayList<String> list = new ArrayList<String>();
        backtrack(list, "", 0, 0, n);
        return list;
    }
    
    public void backtrack(List<String> list, String in, int open, int close, int max){
        if (in.length() == max*2) {
            list.add(in);
            return;
        }
        
        if (open < max) 
            backtrack (list, in + "(", open + 1, close,max);
        if (close < open) 
            backtrack (list, in + ")", open, close+1, max);   
    }
}
