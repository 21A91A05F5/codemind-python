n=input()
k=input()
s="aeiouAEIOU"
c=-1
for i in range(len(n)):
    if n[i]==k:
        c=i
        break
if(c>-1):
    print(True)
    print(c)
else:
    print(False)