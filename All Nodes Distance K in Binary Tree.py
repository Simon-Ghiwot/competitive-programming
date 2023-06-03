class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_all_below(root, depth, ans, final):
            if root == None:
                return
            if depth == final:
                ans.append(root.val)
                return
            add_all_below(root.left, depth + 1, ans, final)
            add_all_below(root.right, depth + 1, ans, final)

        def dfs(root, depth, ans):
            if root == None:
                return [False, depth]
            if root == target:
                new_found = True
                add_all_below(root, 0, ans, k)
                return [True, depth]
            ok, d = dfs(root.left, depth + 1, ans)
            if ok:
                if k - (d - depth) == 0:
                    ans.append(root.val)
                else:
                    add_all_below(root.right, 0, ans, k - (d - depth) - 1)
                return [True, d]
            ok, d = dfs(root.right, depth + 1, ans)
            if ok:
                if k - (d - depth) == 0:
                    ans.append(root.val)
                else:
                    add_all_below(root.left, 0, ans, k - (d - depth) - 1)
                return [True, d]
            return [False, depth]
            
        ans, res = [], []
        dfs(root, 0, ans)
        for i in ans:
            if i != target.val:
                res.append(i)
        if k == 0:
            res.append(target.val)
        return list(set(res))
