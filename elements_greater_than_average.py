n=int(input())
a=list(map(int,input().split()))
k=(sum(a))//n
p=0
for i in a:
    if i>=k :
        p+=1
print(p)