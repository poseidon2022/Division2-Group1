class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my_list = list()
        while head:
            my_list.append(head.val)
            head = head.next
        return my_list==my_list[::-1]
