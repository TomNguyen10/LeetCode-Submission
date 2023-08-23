class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> radiantQueue = new LinkedList<>();
        Queue<Integer> direQueue = new LinkedList<>();

        for (int i = 0; i < senate.length(); i++) {
            if (senate.charAt(i) == 'R') {
                radiantQueue.add(i);
            } else {
                direQueue.add(i);
            }
        }

        while (!radiantQueue.isEmpty() && !direQueue.isEmpty()) {
            int radiantIndex = radiantQueue.poll();
            int direIndex = direQueue.poll();
            
            if (radiantIndex < direIndex) {
                radiantQueue.add(radiantIndex + senate.length());  
            } else {
                direQueue.add(direIndex + senate.length()); 
            }
        }

        return radiantQueue.isEmpty() ? "Dire" : "Radiant";

    }
}
