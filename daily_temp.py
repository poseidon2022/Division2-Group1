class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = list()
        num_stack = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while my_stack and temperatures[my_stack[-1]]<temperatures[i]:
                num_stack[my_stack[-1]] = i - my_stack[-1] 
                my_stack.pop()
            my_stack.append(i)
        return num_stack