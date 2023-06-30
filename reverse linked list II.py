class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head
        dummy2 = head
        right2 = right
        mine = list()
        while dummy!=None:
            mine.append(dummy.val)
            dummy = dummy.next
        i = 1
        while head!=None:
            if i>=left and i<=right:
                head.val = mine[right2-1]
                right2-=1
            i+=1
            head = head.next
        return dummy2