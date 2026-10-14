arr=list(map(int,input().split(" ")))
c=0
n=len(arr)
for i in range(0,n):
    if arr[i]%3==0:
        print(arr[i-1])
        break