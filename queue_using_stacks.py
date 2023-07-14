class MyQueue:

    def __init__(self):
        self.stack_front = list()
        self.stack_back = list()
    def push(self, x: int) -> None:
        self.stack_back.insert(0,x)

    def pop(self) -> int:
        if not self.stack_front:
            while self.stack_back:
                self.stack_front.insert(0,self.stack_back.pop(0))
        return self.stack_front.pop(0)
    def peek(self) -> int:
        if not self.stack_front:
            while self.stack_back:
                self.stack_front.insert(0,self.stack_back.pop(0))
        return self.stack_front[0]

    def empty(self) -> bool:
        return not self.stack_back and not self.stack_front
        