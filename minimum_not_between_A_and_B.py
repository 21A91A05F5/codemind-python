n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in s:
    if i not in range(a,b+1):
        c.append(i)
if c!=[] :
    print(min(c))
else:
    print("-1")