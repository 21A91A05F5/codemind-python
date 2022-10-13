n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(1,len(a)-1):
    if a[i-1]%2==0 and a[i]%2==0 and a[i+1]%2==0 :
        k+=1
print(k)