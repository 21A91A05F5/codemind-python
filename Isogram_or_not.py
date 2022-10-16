s=input()
#s=s.lower()
k=0
for i in s:
    if s.count(i)==1:
        k+=1
if k==len(s) :
    print(True)
else:
    print(False)