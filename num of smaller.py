msg = input()
arr1 = input().split(' ')
arr2 = input().split(' ')
ans = list()
i = 0
j = 0
count = 0
while i<len(arr1) and j<len(arr2):
    if int(arr1[i])<int(arr2[j]):
        count+=1
        i+=1
    elif int(arr1[i])>=int(arr2[j]):
        j+=1
        ans.append(count)
while j<len(arr2):
    ans.append(count)
    j+=1
for i in ans:
    print(i,end =" ")