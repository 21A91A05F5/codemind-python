def prime(a):
    for i in range(2,int(a**0.5)) :
        if a%i==0 :
            return 0
    else:
        return 1
n=int(input())
k=0
for i in range(2,n):
    for j in range(i+1,n):
        if i*j==n :
            if prime(i) and prime(j) :
                k=1
                print(i,j,end=" ")
if k==0:
    print("-1")