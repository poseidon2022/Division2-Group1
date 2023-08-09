class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = list()
        def path(root,_str):
            if not root.right and not root.left:
                _str+=str(root.val)
                ans.append(_str)
                return
            _str+=str(root.val) + "->"
            if root.left: path(root.left,_str)
            if root.right: path(root.right,_str)
        
        path(root,"")
        return ans