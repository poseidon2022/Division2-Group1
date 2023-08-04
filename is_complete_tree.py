class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        Nullify = False
        while queue:
            size = len(queue)
            for i in range(size):
                k = queue.popleft()
                if Nullify and k!=None: return False
                if k:
                    queue.append(k.left)
                    queue.append(k.right)
                else:
                    if Nullify==False: Nullify = not Nullify

        return True