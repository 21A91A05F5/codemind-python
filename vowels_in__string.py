s=input()
v="AEIOUaeiou"
b=[]
for i in s:
    if i in v and i not in b:
        b.append(i)
if len(b)==0:
    print(0)
else:
    print(*b)