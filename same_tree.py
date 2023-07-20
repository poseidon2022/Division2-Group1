class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = list()
        def same(root):
            if not root:
                ans.append(None)
                return

            ans.append(root.val)
            same(root.left)
            same(root.right)
        same(p)
        same(q)
        n = len(ans)
        return ans[:n//2] == ans[n//2:]