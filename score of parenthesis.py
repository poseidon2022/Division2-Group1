class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        my_stack = list()
        prev = 0
        count = 0
        for i in s:
            if i=='(':
                prev=0
                my_stack.append(i)
                continue
            elif prev==0 and i==')':
                prev+=1
                count+=(2**(len(my_stack)-1))
            my_stack.pop()
        return count