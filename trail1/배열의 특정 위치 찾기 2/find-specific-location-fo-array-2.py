arr=list(map(int,input().split(" ")))
evens=arr[1::2]
odds=arr[0::2]
e=sum(evens)
o=sum(odds)
if e>=o:
    print(e-o)
else:
    print(o-e)