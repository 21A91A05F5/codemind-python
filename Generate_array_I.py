n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if i%2==0 :
        for j in range(1,a[i+1]+1):
            print(a[i],end=' ')