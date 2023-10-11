t = int(input())
for _ in range(t):
    n,c = map(str,input().split())
    inp = 2*input()
    if c=='g':
        print(0)
        continue
    _count = float('-inf')
    cur = 0
    for i in inp:
        if i=='g':
            if cur>_count: _count = cur
            cur = 0
            continue
        if i==c:
            cur+=1
            continue
        if cur>0:
            cur+=1
    print(_count)
        