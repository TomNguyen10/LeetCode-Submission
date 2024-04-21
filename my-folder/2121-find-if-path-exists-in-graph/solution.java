class Solution {

    Map<Integer, Set<Integer>> map = new HashMap<>();

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) {
            return true; 
        }

        for (int[] edge : edges) {
            if (!map.containsKey(edge[0])) {
                map.put(edge[0], new HashSet<>());
            }
            map.get(edge[0]).add(edge[1]);
            if (!map.containsKey(edge[1])) {
                map.put(edge[1], new HashSet<>());
            }
            map.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();
        
        return dfs(source, destination, visited);
    }

    private boolean dfs(int current, int destination, Set<Integer> visited) {
        if (current == destination) {
            return true; 
        }
        visited.add(current);
        if (map.containsKey(current)) {
            for (int neighbor : map.get(current)) {
                if (!visited.contains(neighbor)) {
                    if (dfs(neighbor, destination, visited)) {
                        return true; 
                    }
                }
            }
        }
        return false; 
    }
}

