class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root: return 0
            return 1 + max(depth(root.right),depth(root.left))
        
        return depth(root)