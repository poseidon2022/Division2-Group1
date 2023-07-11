class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        dummy1 = l1
        dum =  l1
        dummy2 = l2
        mine = list()
        while True:
            if l1 and l2:
                mine.append((l1.val + l2.val +  rem)%10)
                if (l1.val + l2.val + rem)>=10:
                    rem = 1
                else: rem = 0
            elif l1 and not l2:
                mine.append((l1.val +  rem)%10)
                if (l1.val + rem)>=10:
                    rem = 1
                else: rem = 0
            elif l2 and not l1:
                mine.append((l2.val +  rem)%10)
                if (l2.val + rem)>=10:
                    rem = 1
                else: rem = 0
            elif not l1 and not l2:
                if rem!=0: mine.append(rem)
                break
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        new = ListNode(mine[0])
        tail = new
        e = 1
        while e<len(mine):
            tail.next = ListNode(mine[e])
            tail = tail.next
            e+=1
        return new
