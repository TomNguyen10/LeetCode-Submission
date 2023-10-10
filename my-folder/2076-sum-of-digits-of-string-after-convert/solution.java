class Solution {
    public int getLucky(String s, int k) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            int i = c - 'a' + 1;
            String add = String.valueOf(i);
            sb.append(add);
        }
        String news = sb.toString();
        for (int i = 0; i < k; i++) {
            int total = 0;
            for (char c : news.toCharArray()) {
                total += Integer.parseInt(String.valueOf(c));
            }
            news = String.valueOf(total);
        }
        return Integer.parseInt(String.valueOf(news));
    }
}
