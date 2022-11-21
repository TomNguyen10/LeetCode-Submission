class Solution {
    public int maxDistance(int[][] grid) {
        
        
        
        // Queue to store all Nodes
        Queue<Node> queue = new LinkedList<>();
        
        boolean flag = true;
        int n = grid.length;
        int m = grid[0].length;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    queue.add(new Node(i,j,0));
                }else{
                    flag = false;
                }
            }
        }
        
        
        // to check if matrix is full of only 0's or only 1's, if so then return -1
        if(queue.isEmpty() || flag){
            return -1;
        }

    
        int max = Integer.MIN_VALUE;
        int delrow[] = {0,1,0,-1};
        int delcol[] = {1,0,-1,0};
        
        // Iterating queue till its empty
        while(!queue.isEmpty()){
            Node node = queue.poll();
            int row = node.row;
            int col = node.col;
            int steps = node.steps;
            max = Math.max(steps,max);
            for(int i=0;i<4;i++){
                int nrow = row + delrow[i];
                int ncol = col + delcol[i];
                
                if(nrow>=0 && ncol>=0 && nrow<n && ncol<m && grid[nrow][ncol]==0){
                    grid[nrow][ncol] = 1;
                    queue.add( new Node(nrow,ncol,steps+1));
                }
            }
        }
        
        
        return max;
        
    }
}

class Node{
    int row;
    int col;
    int steps;
    Node(int row,int col,int steps){
        this.row = row;
        this.col = col;
        this.steps = steps;
    }
}
