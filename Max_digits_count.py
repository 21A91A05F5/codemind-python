n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    m=i;
    c=0
    while i :
        d=i%10
        i=i//10
        c+=1
    b.append(c)
k=max(b)
p=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if b[j]==k :
            p+=1
print(p//n)