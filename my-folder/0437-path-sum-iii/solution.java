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

    public int pathSum(TreeNode root, int targetSum) {
        if(root==null){
            return 0;
        }
       long temp=targetSum;
 

       return  helper(root,temp)+ pathSum(root.left,targetSum)+ pathSum(root.right,targetSum);
    } 
    public int helper(TreeNode root, long target){
       
        if(root==null){
            return 0;
        } 
       
        int ans=0;
        if(target==(long)root.val){
            ans++;
        }
         ans+=helper(root.left,target-(long)root.val); 
         ans+=helper(root.right,target-(long)root.val);
       
        return ans;
    }
}
