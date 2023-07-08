class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        mine = deque()
        for i in range(len(tickets)):
            mine.append((tickets[i],i))
        i = 0
        time = 0
        while True:
            if mine[i][0]==1:
                time+=1
                if mine[i][1]==k: break
                mine.popleft()
            else:
                time+=1
                mine[i] = (mine[i][0]-1,mine[i][1])
                mine.append(mine[i])
                mine.popleft()
        return time