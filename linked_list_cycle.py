class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mine = defaultdict(lambda:0)
        while head!=None:
            mine[head]+=1
            if mine[head]>1:
                return True
            head = head.next
        return False