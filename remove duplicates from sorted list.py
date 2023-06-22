class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = list()
        dummy = head
        while head:
            my_list.append(head.val)
            while head.next!=None and head.next.val in my_list:
                head.next = head.next.next
            head = head.next
        return dummy