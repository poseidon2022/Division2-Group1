class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.ele = k
        self.count = 0
    def enQueue(self, value: int) -> bool:
        if self.count<self.ele:
            self.count+=1
            self.queue.append(value)
            return True
        return False
    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            self.count-=1
            return True
        return False
    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1
    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1
    def isEmpty(self) -> bool:
        return len(self.queue)==0
    def isFull(self) -> bool:
        return len(self.queue)==self.ele