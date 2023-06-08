class Solution {
    public ArrayList<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<String>();
        backtrack(res, "", 0, 0, n);
        return res;
    }
    
    public void backtrack(List<String> list, String input, int open, int close, int max){
        if (input.length() == max*2) {
            list.add(input);
            return;
        }
        
        if (open < max) backtrack (list, input + "(", open+1, close,max);
        if (close < open) backtrack (list, input + ")", open, close+1, max);   
    }
}
