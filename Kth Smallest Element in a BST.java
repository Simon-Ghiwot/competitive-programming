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
    public int kthSmallest(TreeNode root, int k) {
        int [] num = new int [2];
        getKthSmallest(root, k , num);
        return num[0];
    }
    public void getKthSmallest(TreeNode root, int k, int [] num){
        if(root == null)
            return;
        getKthSmallest(root.left, k, num);
        if(++num[1] == k){
            num[0] = root.val;
            return;
        }
        getKthSmallest(root.right, k, num);
    } 
}
