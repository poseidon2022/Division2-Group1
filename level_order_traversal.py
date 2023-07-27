class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = list()
        arr = []
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curNode = queue.popleft()
                if curNode:
                    arr.append(curNode.val)
                    queue.append(curNode.left)
                    queue.append(curNode.right)
            if arr: ans.append(arr)
            arr = []
        return ans