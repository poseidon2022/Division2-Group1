class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = head
        dummy2 = head
        lesser = list()
        greater = list()
        while dummy!=None:
            if dummy.val>=x:
                greater.append(dummy.val)
            else:
                lesser.append(dummy.val)
            dummy = dummy.next
        tgthr = lesser + greater
        count = 0
        while head!=None:
            head.val = tgthr[count]
            count+=1
            head = head.next
        return dummy2