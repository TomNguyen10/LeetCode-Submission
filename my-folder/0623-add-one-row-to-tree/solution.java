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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (root == null || depth == 1) {
            TreeNode node = new TreeNode(val);
            node.left = root;
            return node;
        } 
        dfs(root, val, depth, 1);
        return root;
    }

    private void dfs(TreeNode root, int val, int depth, int current) {
        if (root == null) {
            return;
        }
        if (depth - current == 1) {
            TreeNode left = root.left;
            TreeNode right = root.right;
            root.left = new TreeNode(val);
            root.right = new TreeNode(val);
            root.left.left = left;
            root.right.right = right;
            return;
        }
        dfs(root.left, val, depth, current+1);
        dfs(root.right, val, depth, current+1);
    }
}
