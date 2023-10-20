class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ""
        stack = []
        operations = []
        s = ""
        do = 0
        for i in path:
            if i=="/":
                operations.append("/")
                if s and len(s)!=do: stack.append(s)
                elif s:
                    if do==2:
                        if stack: stack.pop()
                    elif do>2: stack.append(s)
                s = ""
                do = 0
            else:
                s+=i
                if i==".": do+=1
        if do==2 and len(s)==do:
            if stack: stack.pop()
        elif s and s!=".": stack.append(s)
        print(operations,stack)
        ans+="/"
        for i in range(len(stack)):
            ans+=stack[i]
            if i!=len(stack)-1: ans+=operations[i]
        return ans