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
    List<List<Integer>> list = new ArrayList<>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null){
            return list;
        }
        helper(root, 0);
        return list;
    }
    public void helper(TreeNode node, int level){
        if(list.size() == level){
            list.add(new ArrayList<>());
        }
        list.get(level).add(node.val);
        level++;
        if(node.left != null){
            helper(node.left, level);
        }
        if(node.right != null){
            helper(node.right, level);
        }
    }
}
