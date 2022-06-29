n=input()
s="aeiou"
b=[]
for i in range(len(n)):
    if n[i] in s and n[i] not in b:
        b.append(n[i])
if len(b)==len(s) :
    print(True)
else:
    print(False)