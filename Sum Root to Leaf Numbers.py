# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sum_):
            if not root:
                return 0
            if not root.left and not root.right:
                return sum_ * 10 + root.val
            total = 0
            total += dfs(root.left, sum_ * 10 + root.val)
            total += dfs(root.right, sum_ * 10 + root.val)

            return total
        return dfs(root, 0)
