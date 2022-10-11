n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
for i in range(len(a)):
    if a[i]%2==0:
        print(n-i-1)
        break
    