# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key<arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
        
        ans = ListNode()
        dummy = ans
        for i in arr:
            ans.next = ListNode(i)
            ans = ans.next
        return dummy.next