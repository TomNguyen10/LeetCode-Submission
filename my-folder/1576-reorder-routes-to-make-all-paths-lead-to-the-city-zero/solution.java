class Solution {
    public int minReorder(int n, int[][] connections) {
        List<List<int[]>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new ArrayList<>());
        }
        for (int[] connection : connections) {
            int a = connection[0];
            int b = connection[1];
            list.get(a).add(new int[]{b, 1});
            list.get(b).add(new int[]{a, 0});
        }
        int[] changes = new int[1];
        dfs(0, -1, list, changes);
        return changes[0];
    }

    private void dfs(int node, int parent, List<List<int[]>> list, int[] changes) {
        for (int[] neighbor : list.get(node)) {
            int neighbors = neighbor[0];
            int direction = neighbor[1];

            if (neighbors != parent) {
                changes[0] += direction;
                dfs(neighbors, node, list, changes);
            }
        }
    }
}
