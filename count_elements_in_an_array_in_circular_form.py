n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
a.append(a[0])
a=a[::-1]
a.append(a[1])
k=0
for i in range(1,len(a)-1):
    if (a[i-1]%2 and a[i+1]%2==0) or (a[i-1]%2==0 and a[i+1]%2):
        k+=1
print(k)