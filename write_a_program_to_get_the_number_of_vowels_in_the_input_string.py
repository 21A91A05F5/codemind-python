s=input()
s=s.lower()
k=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
        k+=1
print(k)