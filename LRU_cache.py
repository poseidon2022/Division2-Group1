class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cont = defaultdict()
        self.rec = deque()
    def get(self, key: int) -> int:
        try:
            k = self.cont[key]
            if key in self.rec: self.rec.remove(key)
            self.rec.append(key)
            return k
        except:
            return -1
    def put(self, key: int, value: int) -> None:
        if self.cap>0:
            prev = len(self.cont)
            self.cont[key] = value
            now = len(self.cont)
            if now>prev: self.cap-=1
        else:
            prev = len(self.cont)
            self.cont[key] = value
            now = len(self.cont)
            if now>prev:
                rem = self.rec.popleft()
                self.cont.pop(rem)
        if key in self.rec: self.rec.remove(key)
        self.rec.append(key)