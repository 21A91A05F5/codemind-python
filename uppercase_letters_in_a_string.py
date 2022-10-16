s=input()
s=s.split()
k=0
for i in s:
    for j in i :
        if j.upper()==j :
            k+=1
print(k)