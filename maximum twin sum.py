class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list = list()
        while head:
            my_list.append(head)
            head = head.next
        maxim = 0
        i = 0
        count = 0
        while count<len(my_list)//2:
            count+=1
            summa = my_list.pop(-1).val + my_list[i].val
            if summa>maxim:
                maxim = summa
            i+=1
        return maxim