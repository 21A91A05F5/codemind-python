n=int(input())
s=0
a=list(map(int,input().split()))
a=set(a)
for j in a:
   s+=j
print(s)