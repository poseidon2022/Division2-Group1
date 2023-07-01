class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        i = 0
        j = 0
        count = 0
        while j<len(s):
            if s[j] not in s[i:j]:
                count = j-i+1
                j+=1
                if count>max:
                    max = count
                continue
            i+=1
            count = 0
        if s==" " or len(s)==1:
            return 1
        return max