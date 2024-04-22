class Solution {

    public int openLock(String[] deadends, String target) {
        Set<String> deadendSet = new HashSet<>();
        for (String s : deadends) {
            deadendSet.add(s);
        }

        if (deadendSet.contains("0000")) {
            return -1; 
        }

        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer("0000");
        visited.add("0000");

        int turns = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String current = queue.poll();
                if (current.equals(target)) {
                    return turns;
                }
                for (String next : getNextStates(current)) {
                    if (!deadendSet.contains(next) && !visited.contains(next)) {
                        queue.offer(next);
                        visited.add(next);
                    }
                }
            }
            turns++;
        }

        return -1; 
    }

    private Set<String> getNextStates(String current) {
        Set<String> nextStates = new HashSet<>();
        char[] digits = current.toCharArray();
        for (int i = 0; i < 4; i++) {
            char original = digits[i];
            digits[i] = (char) (((digits[i] - '0' + 1) % 10) + '0');
            nextStates.add(new String(digits));
            digits[i] = (char) (((original - '0' + 9) % 10) + '0');
            nextStates.add(new String(digits));
            digits[i] = original;
        }
        return nextStates;
    }
}

