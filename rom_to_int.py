class Solution:
    def romanToInt(self, s: str) -> int:
        roman = dict()
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        i = 0
        while i<len(s):
            if i<len(s)-1 and s[i]=='I' and s[i+1]=='V':
                sum+=(roman['V'] - roman['I'])
                i+=2
            elif i<len(s)-1 and s[i]=='I' and s[i+1]=='X':
                sum+=(roman['X'] - roman['I'])
                i+=2
            elif i<len(s)-1 and s[i]=='X' and s[i+1]=='L':
                sum+=(roman['L'] - roman['X'])
                i+=2
            elif i<len(s)-1 and s[i]=='X' and s[i+1]=='C':
                sum+=(roman['C'] - roman['X'])
                i+=2
            elif i<len(s)-1 and s[i]=='C' and s[i+1]=='D':
                sum+=(roman['D'] - roman['C'])
                i+=2
            elif i<len(s)-1 and s[i]=='C' and s[i+1]=='M':
                sum+=(roman['M'] - roman['C'])
                i+=2
            else:
                sum+=roman[s[i]]
                i+=1
        return sum