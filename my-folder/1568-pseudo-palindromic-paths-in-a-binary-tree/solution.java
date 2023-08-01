/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pseudoPalindromicPaths(TreeNode root) {
        return dfs(root, new HashSet<>());
    }

    private int dfs(TreeNode root, Set<Integer> set) {
        if (root == null) {
            return 0;
        }
        if (set.contains(root.val)) {
            set.remove(root.val);
        }
        else {
            set.add(root.val);
        }
        if(root.left==null&& root.right==null){
            return set.size()<=1?1:0; 
        }
        return dfs(root.left, new HashSet<>(set)) + dfs(root.right, new HashSet<>(set));
    }
}
