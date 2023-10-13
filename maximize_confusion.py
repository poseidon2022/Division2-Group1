class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = []
        def confuse(boolean,k):
            i,j = 0,0
            count = 0
            while j<len(answerKey):
                if answerKey[j]==boolean: count+=1
                elif answerKey[j]!=boolean:
                    if k>0:
                        k-=1
                        count+=1
                    else:
                        ans.append(count)
                        while k<1:
                            if answerKey[i]!=boolean: k+=1
                            count-=1
                            i+=1
                        continue
                j+=1
            ans.append(count)
        confuse('T',k)
        confuse('F',k)
        return max(ans)