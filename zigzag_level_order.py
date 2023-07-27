class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = list()
        arr = []
        helper = True
        while queue:
            size = len(queue)
            for i in range(size):
                curNode = queue.popleft()
                if curNode:
                    arr.append(curNode.val)
                    queue.append(curNode.left)
                    queue.append(curNode.right)
            if arr:
                if helper==True: ans.append(arr)
                else: ans.append(arr[::-1])
            arr = []
            helper = not helper
        return ans