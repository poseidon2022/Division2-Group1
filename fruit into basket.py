class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket1 = list()
        basket2 = list()
        i, j, maxim, count = 0, 0, 0, 0
        while j<len(fruits):
            if not basket1 or (basket1 and basket1[-1]==fruits[j]):
                basket1.append(fruits[j])
                count+=1
                j+=1
            elif not basket2 or (basket2 and basket2[-1]==fruits[j]):
                basket2.append(fruits[j])
                count+=1
                j+=1
            else:
                if count>maxim:
                    maxim = count
                if fruits[i]==basket1[-1]:
                    basket1.pop()
                elif fruits[i]==basket2[-1]:
                    basket2.pop()
                i+=1
                count-=1
        if count>maxim:
            maxim = count
        return maxim