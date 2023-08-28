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
        int max = Integer.MIN_VALUE, maxLevel = 1;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int level = 1;
        while (!q.isEmpty()) {
            int sum = 0;
            for (int size = q.size(); size > 0; size--) {
                TreeNode tree = q.poll();
                sum += tree.val;
                if (tree.left != null) {
                    q.offer(tree.left);
                }
                if (tree.right != null) {
                    q.offer(tree.right);
                }
            }
            if (max < sum) {
                max = sum;
                maxLevel = level;
            }
            level++;
        }
        return maxLevel;
    }
}
