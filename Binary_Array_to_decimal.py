n=int(input())
a=list(map(int,input().split()))
p=0
k=0
a=a[::-1]
for i in a:
    p=p+i*(2**k)
    k+=1
print(p)