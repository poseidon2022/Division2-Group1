class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        ans = ListNode(head.val)
        dummy = head
        head = head.next
        final = ans
        count = 2
        while head!=None:
            if (count%2)!=0:
                ans.next = ListNode(head.val)
                ans = ans.next
            head = head.next
            count+=1
        count = 1
        while dummy!=None:
            if (count%2)==0:
                ans.next = ListNode(dummy.val)
                ans = ans.next
            dummy = dummy.next
            count+=1
        return final