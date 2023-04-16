# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans, que = 0, deque()
        que.append([root, 0])
        while que:
            left, right = inf, -inf
            for i in range(len(que)):
                current, parent = que.popleft()
                left = min(left, parent)
                right = max(right, parent)
                if current.left:
                    que.append([current.left, parent * 2 + 1])
                if current.right:
                    que.append([current.right, parent * 2 + 2])
            ans = max(ans, right - left + 1)
        
        return ans
