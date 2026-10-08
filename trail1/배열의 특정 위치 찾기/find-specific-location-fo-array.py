arr=list(map(int,input().split()))
n=len(arr)
sum1=0
sum2=0
a=0
for i in range(1,n,2):
    sum1+=arr[i]
for i in range(2,n,3):
    sum2+=arr[i]
    a+=1
sum2=sum2/a
print(sum1,f"{sum2:.1f}")