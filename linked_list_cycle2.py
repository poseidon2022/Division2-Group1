class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mine = defaultdict(lambda:0)
        while head!=None:
            mine[head]+=1
            if mine[head]>1:
                return head
            temp = head
            head = head.next