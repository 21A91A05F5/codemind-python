n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(1,len(a)-1):
    if a[i-1]%2 and a[i]%2 and a[i+1]%2 :
        s+=1
print(s)