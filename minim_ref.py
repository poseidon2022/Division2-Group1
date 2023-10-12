class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i = 0
        j = len(plants)-1
        ref = 0
        initA,initB = capacityA,capacityB
        while i<=j:
            prevCapA = capacityA
            prevCapB = capacityB
            if i==j:
                now = max(capacityA,capacityB)
                if now>plants[i]:capacityA-=plants[i]
                if now<plants[i]:ref+=1 
                i+=1
                j-=1
                continue
            if capacityA>=plants[i]:
                capacityA-=plants[i]
            if capacityB>=plants[j]:
                capacityB-=plants[j]
            if prevCapA<plants[i]:
                capacityA = initA
                capacityA-=plants[i]
                ref+=1
            if prevCapB<plants[j]:
                capacityB = initB
                capacityB-=plants[j]
                ref+=1 
            i+=1
            j-=1
        return ref