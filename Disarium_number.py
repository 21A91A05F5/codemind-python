def count(n):
    k=0
    while n:
        d=n%10
        n=n//10
        k+=1
    return k
n=int(input())
k=count(n)
m=n
r=0
while n:
    d=n%10
    n=n//10
    r=r+pow(d,k)
    k-=1
if r==m :
    print(True)
else:
    print(False)