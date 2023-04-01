# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        
        total = [0]
        def dfs(root, total, sum_, prefix, target):
            if not root:
                return
            
            sum_ += root.val
            total[0] += prefix[sum_ - target]
            prefix[sum_] += 1
            
            dfs(root.left, total, sum_, prefix, target)
            dfs(root.right, total, sum_, prefix, target)

            prefix[sum_] -= 1
            sum_ -= root.val

        dfs(root, total, 0, prefix, targetSum)

        return total[0]

            
