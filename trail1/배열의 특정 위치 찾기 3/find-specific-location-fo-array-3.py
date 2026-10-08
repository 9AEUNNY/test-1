arr=list(map(int,input().split()))
a=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        a+=1
    else:
        arr2=arr[:a]
        break
print(sum(arr2[-3:]))