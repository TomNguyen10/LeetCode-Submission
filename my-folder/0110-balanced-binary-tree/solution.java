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
   private int helper(TreeNode root, int height) {
        if (root == null) {
            return height;
        }
        
        int leftTree = helper(root.left, height + 1);
        int rightTree = helper(root.right, height + 1);
        if (leftTree < 0 || rightTree < 0 || Math.abs(leftTree - rightTree) > 1) {
            return -1;
        }
        
        return Math.max(leftTree, rightTree);
    }

    public boolean isBalanced(TreeNode root) {
        return helper(root, 0) >= 0;
    }
}
