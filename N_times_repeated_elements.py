n=int(input())
a=list(map(int,input().split()))
k=int(input())
p=[]
for i in a:
    if a.count(i)==k and i not in p:
        p.append(i)
if len(p)==0:
    print(-1)
else:
    print(*p)