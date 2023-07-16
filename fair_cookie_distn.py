class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minUnfairness = float('inf')
        bucket = [0]*k
        
        def cookie(i,bucket):
            if i==len(cookies) and max(bucket)<self.minUnfairness:
                self.minUnfairness = max(bucket)
                return
            if i==len(cookies): return
            if k==len(cookies):
                self.minUnfairness = max(cookies)
                return
            for j in range(k):
                bucket[j]+=cookies[i]
                cookie(i+1,bucket)
                bucket[j]-=cookies[i]
        
        cookie(0,bucket)
        return self.minUnfairness