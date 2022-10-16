s=input()
s=s.lower()
s=s.split()
k="aeiou"
for i in s:
    b=[]
    for j in i:
        if j in k and j not in b :
            b.append(i)
    print(len(b),end=" ")