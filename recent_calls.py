class RecentCounter:

    def __init__(self):
        self.recent = deque()
    def ping(self, t: int) -> int:
        self.recent.appendleft(t)
        count = 0
        for i in self.recent:
            if i>=t-3000 and i<=t:
                count+=1
            else: break
        return count