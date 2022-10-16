s=input()
s=s.lower()
k="abcdefghijklmnopqrstuvwxyz "
p=0
for i in s:
    if i not in k:
        p+=1
print(p)