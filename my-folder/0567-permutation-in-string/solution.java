class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s1.length() > s2.length()) {
            return false;
        }

        Map<Character, Integer> m1 = new HashMap<>();
        Map<Character, Integer> m2 = new HashMap<>();

        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            m1.put(c1, m1.getOrDefault(c1, 0) + 1);
            m2.put(c2, m2.getOrDefault(c2, 0) + 1);
        }

        if (m1.equals(m2)) return true;

        for (int right = s1.length(); right < s2.length(); right++) {
            int left = right - s1.length();
            char cRemove = s2.charAt(left);
            m2.put(cRemove, m2.get(cRemove) - 1);
            if (m2.get(cRemove) == 0) {
                m2.remove(cRemove);
            }
            char cAdd = s2.charAt(right);
            m2.put(cAdd, m2.getOrDefault(cAdd, 0) + 1);
            if (m1.equals(m2)) {
                return true;
            }
        }
        return false;
    }
}

