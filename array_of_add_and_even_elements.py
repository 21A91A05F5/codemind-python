n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i%2 :
        b.append(i)
    else:
        c.append(i)
b=b+c
print(*b)