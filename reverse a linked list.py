class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = list()
        another = list()
        dummy = head
        while head:
            my_list.append(head.val)
            head = head.next
        i = 0
        my_list.reverse()
        while dummy:
            dummy.val = my_list[i]
            another.append(dummy)
            dummy = dummy.next
            i+=1
        if another:
            return another[0]