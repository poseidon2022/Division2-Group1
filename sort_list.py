class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = list()
        dummy = head
        dummy2 = dummy
        while head:
            my_list.append(head.val)
            head = head.next
        my_list.sort()
        i = 0
        while dummy:
            dummy.val = my_list[i]
            i+=1
            dummy = dummy.next
        return dummy2