n=int(input())
s=0
a=list(map(int,input().split()))
a=set(a)
for j in a:
   if j%2==0 :
       s+=1
print(s)