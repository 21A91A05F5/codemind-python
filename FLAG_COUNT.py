n=int(input())
w=0
r=2
for i in range(n):
    k=w
    w=r
    r+=k
print(w)
