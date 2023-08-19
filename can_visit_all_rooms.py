class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        mine = set()
        while queue:
            n = len(queue)
            for i in range(n):
                k = queue.popleft()
                if k in mine: continue
                queue+=rooms[k]
                if k!=0: mine.add(k)
                if len(mine)==len(rooms)-1: return True
                

        return False