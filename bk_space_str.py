class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t_list = list()
        s_list = list()
        for i in s:
            if not s_list and i=='#': continue
            elif i!='#': s_list.append(i)
            elif s_list and i=='#': s_list.pop()
        for i in t:
            if not t_list and i=='#': continue
            elif i!='#': t_list.append(i)
            elif t_list and i=='#': t_list.pop()
        return t_list==s_list