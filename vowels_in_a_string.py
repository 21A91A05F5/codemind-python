s=input()
k=input()
p=0
for i in range(len(s)):
    if s[i]==k:
        print(True)
        print(i)
        p=1
        break
if p!=1 :
    print(False)