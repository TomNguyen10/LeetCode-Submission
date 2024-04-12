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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        boolean isLeft = true;
        Queue<TreeNode> d = new LinkedList<>();
        d.offer(root);
        while (!d.isEmpty()) {
            int size = d.size();
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = d.poll();
                if (isLeft) {
                    temp.add(node.val);
                }
                else {
                    temp.add(0, node.val);
                }
                if (node.left != null) {
                    d.add(node.left);
                }
                if (node.right != null) {
                    d.add(node.right);
                }
            }
            res.add(temp);
            isLeft = !isLeft;
        }
        return res;
    }
}
