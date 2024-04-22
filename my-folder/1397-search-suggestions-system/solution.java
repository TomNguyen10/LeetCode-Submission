class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : searchWord.toCharArray()) {
            sb.append(c);
            String current = sb.toString();
            List<String> temp = new ArrayList<>();
            for (String s : products) {
                if (s.startsWith(current)) {
                    temp.add(s);
                }
                if (temp.size() == 3) {
                    break;
                }
            }
            res.add(temp);
        }
        return res;
    }
}
