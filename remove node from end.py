class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        my_list = list()
        dummy = head
        count = 0
        while head:
            head = head.next
            count+=1
        demo = count
        count-=(n-1)
        i = 1
        while dummy:
            if i==count-1:
                dummy.next = (dummy.next).next
                my_list.append(dummy)
                i+=2
                continue
            if i==count:
                dummy = dummy.next
                i+=1
                continue
            my_list.append(dummy)
            dummy = dummy.next
            i+=1
        if my_list:
            return my_list[0]