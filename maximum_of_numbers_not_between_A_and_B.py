n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
p=[]
t=[]
for i in range(a,b+1):
    p.append(i)
for i in s:
    if i not in p:
        t.append(i)
        c=1
if c==0 :
    print("-1")
else:
    print(max(t))