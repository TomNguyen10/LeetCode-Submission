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

    public int[] dfs(TreeNode root) {
        int[] res = new int[2];
        if (root == null) {
            res[0] = 1;
            return res;
        }

        int[] left = dfs(root.left);
        int[] right = dfs(root.right);
        if (left[0] == 1 && right[0] == 1 && Math.abs(left[1] - right[1]) <=1) {
            res[0] = 1;
        }
        res[1] = 1 + Math.max(left[1], right[1]);
        return res;
    }

    public boolean isBalanced(TreeNode root) {
        int[] arr = dfs(root);
        return arr[0] == 1;
    }
}
