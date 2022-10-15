n=int(input())
a=list(map(int,input().split()))
k=0
s=0
for i in range(len(a)//2):
    k=k+a[i]
for i in range(len(a)//2,len(a)):
    s=s+a[i]
print(k)
print(s)