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

    int maxLength = 0;

    public int longestZigZag(TreeNode root) {
        if (root == null) return 0;
        dfs(root, true, 0);
        dfs(root, false, 0);
        return maxLength;
    }

    private void dfs (TreeNode root, boolean isLeft, int length) {
        if (root == null) return;
    
        maxLength = Math.max(maxLength, length);

        if (isLeft) {
            dfs(root.left, false, length+1);
            dfs(root.right, true, 1);
        }
        else {
            dfs(root.right, true, length+1);
            dfs(root.left, false, 1);
        }
    }
}
