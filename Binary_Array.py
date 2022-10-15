n=int(input())
a=list(map(int,input().split()))
p=0
for i in a:
    if i==0 or i==1 :
        p+=1
if p==len(a) :
    print(True)
else:
    print(False)