# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if root == None:
                return ""
            if root.left == None and root.right == None:
                return str(root.val)

            cur = str(root.val)
            left = right = ""

            left = dfs(root.left)
            right = dfs(root.right)
            if right:
                right = "(" + right + ")"

            return cur + "("+ left + ")" + right

        return dfs(root)
            
