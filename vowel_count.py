n=input()
s="aeiouAEIOU"
c=0
for i in range(len(n)):
    if n[i] in s:
        c+=1
print(c)