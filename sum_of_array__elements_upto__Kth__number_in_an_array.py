n=int(input())
s=0
a=list(map(int,input().split()))
k=int(input())
p=0
for j in a:
    s+=1
    p=p+j
    if s==k :
        break
print(p)