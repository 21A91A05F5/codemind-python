n=int(input())
m=int(input())
s=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in m:
        s=s+i
print(s)