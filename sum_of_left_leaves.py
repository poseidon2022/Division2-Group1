class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        mine = deque([root])
        sum = 0
        while mine:
            curNode = mine.popleft()
            if curNode:
                if curNode.left!=None and (curNode.left.left==None and curNode.left.right==None): sum+=curNode.left.val
                mine.append(curNode.left)
                mine.append(curNode.right)
        return sum