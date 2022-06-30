n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2==0 and a.count(i)>=1 :
        if i not in b:
            b.append(i)
print(len(b))