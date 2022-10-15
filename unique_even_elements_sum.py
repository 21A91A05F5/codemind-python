n=int(input())
a=list(map(int,input().split()))
a=set(a)
k=0
for i in a:
    if i%2==0 :
        k=k+i
print(k)