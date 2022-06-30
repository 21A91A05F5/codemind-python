n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in s:
    if i in range(a,b+1):
        c.append(i)
if c!=[] :
    print(max(c))
else:
    print("-1")