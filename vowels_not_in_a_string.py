n=input()
n=n.lower()
s="aeiou"
c=0
b=[]
for i in n:
    if i in s and i not in b:
        c+=1
        b.append(i)
if(c<len(s)-1) :
    for i in s:
        if i not in b:
            print(i,end=' ')
if len(b)==len(s):
    print("0")
