n=int(input())
for i in range(n):
    c=0
    m=int(input())
    a=list(map(int,input().split()))
    for j in range(1,m):
        if a[j-1]>a[j]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(a)-min(a))
        