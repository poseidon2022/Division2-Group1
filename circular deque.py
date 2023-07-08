class MyCircularDeque:

    def __init__(self, k: int):
        self.my_deque = list()
        self.k = k
    def insertFront(self, value: int) -> bool:
        if len(self.my_deque)<self.k:
            self.my_deque.append(value)
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.my_deque)<self.k:
            self.my_deque.reverse()
            self.my_deque.append(value)
            self.my_deque.reverse()
            return True
        return False
    def deleteFront(self) -> bool:
        if len(self.my_deque)>0:
            self.my_deque.pop()
            return True
        return False
    def deleteLast(self) -> bool:
        if len(self.my_deque)>0:
            self.my_deque.reverse()
            self.my_deque.pop()
            self.my_deque.reverse()
            return True
        return False
    def getFront(self) -> int:
        if len(self.my_deque)>0:
            return (self.my_deque)[len(self.my_deque)-1]
        return -1
    def getRear(self) -> int:
        if len(self.my_deque)>0:
            self.my_deque.reverse()
            d = (self.my_deque)[len(self.my_deque)-1]
            self.my_deque.reverse()
            return d
        return -1
    def isEmpty(self) -> bool:
        return len(self.my_deque)==0
    def isFull(self) -> bool:
        return len(self.my_deque)==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()