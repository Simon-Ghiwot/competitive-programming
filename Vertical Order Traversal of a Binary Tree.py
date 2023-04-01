# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns_dict = defaultdict(list)
        result = []

        def dfs(root, row, col, columns_dict):
            if not root:
                return
            columns_dict[col].append([row, root.val])
            dfs(root.left, row + 1, col - 1, columns_dict)
            dfs(root.right, row + 1, col + 1, columns_dict)

            return
        

        dfs(root, 0, 0, columns_dict)
        # sort the keys in ascending word
        keys = sorted(columns_dict.keys())
        for key in keys:
            # then sort values of the dict in ascending order first by row then by by val 
            sorted_val = sorted(columns_dict[key])
             # store the val in the answer
            cur = []
            for row, val in sorted_val:
                cur.append(val)
            result.append(cur)

        return result
