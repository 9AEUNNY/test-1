n=int(input())
arr=list(map(int,input().split(" ")))
new=[elem**2 for elem in arr]
for i in new:
    print(i, end=" ")