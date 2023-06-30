class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        if list1!=None and list2==None:
            return list1
        if list1==None and list2!=None:
            return list2

        dummy = list1
        dummy2 = list2
        dummy3 = list1
        my_list = list()
        while list1!=None or list2!=None:
            if list1!=None:
                my_list.append(list1.val)
                list1 = list1.next
                continue
            if list2!=None:
                my_list.append(list2.val)
                list2 = list2.next
                continue
        my_list.sort()
        count = 0
        countt = 0
        while dummy!=None:
            if dummy.next!=None:
                dummy.val = my_list[count]
                dummy = dummy.next
            elif dummy.next==None:
                dummy.val = my_list[count]
                if countt == 0:
                    dummy.next = dummy2
                    countt+=1
                dummy = dummy.next
            count+=1
        return dummy3