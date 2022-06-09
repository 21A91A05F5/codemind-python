n=int(input())
snum=str(n)
k=1
for i in snum :
    if snum.count(i)>1:
        k=0
        break
if k==0 :
    print("Not Unique Number")
else:
    print("Unique Number")