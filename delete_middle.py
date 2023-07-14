class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        dummy = head
        dummy2 = head
        while head!=None:
            count+=1
            head = head.next
        if count==1:
            return dummy2.next
        middle = count//2
        index = 0
        while dummy!=None:
            if middle-1==index:
                dummy.next = dummy.next.next
            index+=1
            dummy = dummy.next
        return dummy2