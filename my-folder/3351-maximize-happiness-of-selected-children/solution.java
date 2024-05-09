class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        long happinessCount = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> -Integer.compare(a,b));
        
        for(int i : happiness){
            pq.offer(i);
        }
        
        long reduction = 0;
        while(k > 0){
            if(pq.peek()-reduction > 0){
                happinessCount += (pq.remove()-reduction);
            }else{
                pq.remove();
            }
            
            reduction++;
            k--;
        }
        
        return happinessCount;
    }
}
