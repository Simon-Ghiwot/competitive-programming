# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return [0, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            total = [left[0] + right[0] + root.val, left[1] + right[1] + 1]
            if total[0] // total[1] == root.val:
                result[0] += 1
            
            return total
        
        dfs(root)
        return result[0]
