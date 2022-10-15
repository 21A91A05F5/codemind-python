n=int(input())
b=list(map(int,input().split()))
if len(b)%2!=0:
    b.append(0)
print(*b)