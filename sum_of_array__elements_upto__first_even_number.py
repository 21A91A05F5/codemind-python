n=int(input())
a=list(map(int,input().split()))
p=0
for j in a:
    if j%2==0 :
        break
    p=p+j
print(p)