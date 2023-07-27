class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        _max = float('-inf')
        queue = deque([[root,_max]])
        count = 0
        while queue:
            curNode = queue.popleft()
            if curNode[0]:
                if curNode[0].val>=curNode[1]:
                    queue.append([curNode[0].left,curNode[0].val])
                    queue.append([curNode[0].right,curNode[0].val])
                    count+=1
                else:
                    queue.append([curNode[0].left,curNode[1]])
                    queue.append([curNode[0].right,curNode[1]])
        return count