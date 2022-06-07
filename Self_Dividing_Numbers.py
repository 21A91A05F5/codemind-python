def self_dividing(i):
    p=i
    h=0
    c=0
    while i :
        d=i%10
        i=i//10
        h+=1
        if d!=0 and p%d==0 :
            c+=1
    if h==c :
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    k=self_dividing(i)
    if k==1 :
        print(i,end=' ')