class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["-","+","*","/"]
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if len(stack)>=2:
                    if i=="*":
                        tempo = stack.pop(-1) * stack.pop(-1)
                        stack.append(tempo)
                    elif i=="-":
                        tempo = stack[-2] - stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(tempo)
                    elif i=="+":
                        tempo = stack.pop(-1) + stack.pop(-1)
                        stack.append(tempo)
                    elif i=="/":
                        tempo = stack[-2] / stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(int(tempo))
        return stack[0]