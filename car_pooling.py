class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mine = []
        for ppl,pick,drop in trips:
            mine.append([pick,ppl,1])
            mine.append([drop,ppl,0])
        
        print(mine)
        mine.sort(key = lambda x: (x[0],x[2]))
        
        curr = 0
        for p,ppl,t in mine:
            if t==1: curr+=ppl
            else: curr-=ppl

            if curr>capacity: return False
        return True