class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = list()
        arr = []
        if root: ans.append(root.val)
        while queue:
            size = len(queue)
            for i in range(size):
                k = queue.popleft()
                if k:
                    if k.left: arr.append(k.left.val)
                    if k.right: arr.append(k.right.val)
                    queue.append(k.left)
                    queue.append(k.right)
            if arr: ans.append(max(arr))
            arr = []
        return ans