class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = list()
        def helper(root,_min,_max):
            if not root: return True


            if root.val>=_min:
                return False
            if root.val<=_max:
                return False

            return helper(root.left,root.val,_max)==True and helper(root.right,_min,root.val)==True
            
        return helper(root,float('inf'),float('-inf'))