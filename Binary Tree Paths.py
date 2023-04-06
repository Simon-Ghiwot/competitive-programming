# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.backtrack(root, [])
        return self.ans
    def backtrack(self, root, current):
        current.append(root.val)
        if root.left == None and root.right == None:
            self.ans.append("->".join(map(str, current)))
            current.pop()
            return
        if root.left:
            self.backtrack(root.left, current)
        if root.right:
            self.backtrack(root.right, current)
        current.pop() 
