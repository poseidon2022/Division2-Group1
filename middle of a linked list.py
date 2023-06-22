class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = list()
        count=0
        while head:
            my_list.append(head)
            head = head.next
            count+=1
        return my_list[count//2]