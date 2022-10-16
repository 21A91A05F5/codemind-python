s=input()
s=list(s.split())
b=[]
for i in range(len(s)):
    b.append(len(s[i]))
print(max(b))