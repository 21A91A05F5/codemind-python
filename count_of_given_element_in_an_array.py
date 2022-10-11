n=int(input())
a=list(map(int,input().split()))
k=int(input())
if k in a :
    print(a.count(k))
else:
    print(0)