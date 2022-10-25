class Solution {
    public int nthUglyNumber(int n) {
        if (n < 0)
            return 0;
        int two = 0;
        int three = 0;
        int five = 0;
        
        List<Integer> seq = new ArrayList<Integer>();
        seq.add(1);
        while (seq.size() < n) {
            int val = Math.min(seq.get(two)*2, Math.min(seq.get(three)*3, seq.get(five)*5));
            seq.add(val);
            if (seq.get(two)*2 == val)
                two++;
            if (seq.get(three)*3 == val)
                three++;
            if (seq.get(five)*5 == val)
                five++;
        }
        return seq.get(seq.size() - 1);
    }
}
