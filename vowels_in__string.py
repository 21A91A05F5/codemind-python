n=input()
s="aeiouAEIOU"
c=0
b=[]
for i in n:
    if i in s and i not in b:
        c=1
        b.append(i)
if c==0 :
    print("-1")
else:
    print(*b)