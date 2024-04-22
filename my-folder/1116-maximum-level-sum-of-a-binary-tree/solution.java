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
    public int maxLevelSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int max = Integer.MIN_VALUE;
        int res = 1;
        int level = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            level++;
            int total = 0;
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                total += curr.val;
                if (curr.left != null) {
                    q.offer(curr.left);
                }
                if (curr.right != null) {
                    q.offer(curr.right);
                }
            }  
            if (total > max) {
                res = level;
                max = total;
            }
        }
        return res;
    }
}
