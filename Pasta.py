n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in b:
    if i in a:
        c.append(i)
if(len(set(c))==m):
    print("Yes")
else:
    print("No")