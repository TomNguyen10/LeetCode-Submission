class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int max = releaseTimes[0];
        List<Character> list = new ArrayList<>();
        list.add(keysPressed.charAt(0));
        for (int i = 1; i < keysPressed.length(); i++) {
            int time = releaseTimes[i] - releaseTimes[i-1];
            if (time < max) continue;
            else {
                if (time > max) {
                    max = time;
                    list = new ArrayList<>();
                }
                list.add(keysPressed.charAt(i));
            }
        }
        int charMax = 0;
        char res = list.get(0);
        for (char c : list) {
            if (c - 'a' > charMax) {
                charMax = c - 'a';
                res = c;
            }
        }
        return res;
    }
}
