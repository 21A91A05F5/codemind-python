n=int(input())
s=0
b=[]
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==i and i not in b:
        b.append(i)
print(len(b))