def superDigit(n, k):
    def digSum(s):
        if len(s)==1:
            return int(s)
        _sum = 0
        for i in s:
            _sum+=int(i)
        return digSum(str(_sum))
    return digSum(str(digSum(n))*k)