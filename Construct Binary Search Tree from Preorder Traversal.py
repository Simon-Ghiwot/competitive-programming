# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        left, right = 0, len(preorder) - 1

        def dfs(preorder, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(preorder[left], None, None)
            
            current = TreeNode(preorder[left], None, None)

            n_left, n_right = left + 1, left + 1
            while n_right <= right and preorder[n_right] < preorder[left]:
                n_right += 1
                
            current.left = dfs(preorder, n_left, n_right - 1)
            current.right = dfs(preorder, n_right, right)

            return current
        
        return dfs(preorder, left, right)
