# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []
        while que:
            cur = []
            for i in range(len(que)):
                at = que.popleft()
                cur.append(at.val)
                if at.left:
                    que.append(at.left)
                if at.right:
                    que.append(at.right)
            ans.append(cur)

        return ans
