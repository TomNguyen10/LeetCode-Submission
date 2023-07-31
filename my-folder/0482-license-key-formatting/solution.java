class Solution {
    public String licenseKeyFormatting(String s, int k) {
        s = s.replace("-", "").toUpperCase();
        StringBuilder sb = new StringBuilder(s);
        int remainder = sb.length() % k;
        
        for (int i = sb.length() - k; i > 0; i -= k) {
            sb.insert(i, '-');
        }
        
        return sb.toString();
    }
}
