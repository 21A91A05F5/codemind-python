s=input()
s=s.split()
c=0
for i in s:
    i=i.lower()
    p=i[::-1]
    if i==p :
        c+=1
print(c)