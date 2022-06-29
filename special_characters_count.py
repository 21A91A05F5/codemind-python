n=input()
n=n.lower()
s="abcdefghijklmnopqrstuvwxyz "
c=0
for i in range(len(n)):
    if n[i] not in s:
        c+=1
print(c)