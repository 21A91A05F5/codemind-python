n=input()
n=n.split()
a=[]
for i in n:
    a.append(len(i))
print(max(a))