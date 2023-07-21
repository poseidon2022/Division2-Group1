class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = list()
        if not root: return False
        def summ(root,_sum):
            if not root: return
            if root.left==None and root.right==None:
                _sum+=root.val
                ans.append(_sum)
                _sum = 0 
                return
            

            _sum+=(root.val)
            summ(root.right,_sum)
            summ(root.left,_sum)

        summ(root,0)
        return targetSum in ans