class Solution:
    def largestInteger(self, num: int) -> int:
        odd,even = [],[]
        _odd,_even = deque(),deque()
        numb = str(num)
        final = ""
        for i in numb:
            if int(i)%2==0: even.append(int(i))
            else: odd.append(int(i))
        while odd:
            heapq._heapify_max(odd)
            _odd.append(heapq._heappop_max(odd))
        while even:
            heapq._heapify_max(even)
            _even.append(heapq._heappop_max(even))
        for i in numb:
            if int(i)%2==0: final+=str(_even.popleft())
            else: final+=str(_odd.popleft())
        return int(final)