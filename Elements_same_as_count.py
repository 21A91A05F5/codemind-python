n=int(input())
s=0
b=[]
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==i and i not in b:
        b.append(i)
        s=1
if s==0:
    print(-1)
else:
    print(*b)