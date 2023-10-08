# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def removeGreaterNodes(head):
            if not head or not head.next:
                return head

            next_head = removeGreaterNodes(head.next)

            if next_head and next_head.val > head.val:
                return next_head
            
            head.next = next_head
            return head
        return removeGreaterNodes(head)