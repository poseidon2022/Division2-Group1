msg = input()
arr1 = input().split(' ')
arr2 = input().split(' ')
ans = list()
i = 0
j = 0
while i<len(arr1) and j<len(arr2):
    if int(arr1[i])<=int(arr2[j]):
        ans.append(int(arr1[i]))
        i+=1
    elif int(arr1[i])>int(arr2[j]):
        ans.append(int(arr2[j]))
        j+=1
while j<len(arr2):
    ans.append(int(arr2[j]))
    j+=1
while i<len(arr1):
    ans.append(int(arr1[i]))
    i+=1
for i in ans:
    print(i,end = ' ')