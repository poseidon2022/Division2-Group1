class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        mine = []
        heapify(mine)
        for i in range(len(lists)):
            while lists[i]!=None:
                heapq.heappush(mine,lists[i].val)
                lists[i] = lists[i].next
        while mine:
            ans.next = ListNode(heapq.heappop(mine))
            ans = ans.next
        return dummy.next