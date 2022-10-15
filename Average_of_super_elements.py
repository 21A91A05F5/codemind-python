n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if a.count(i)==i and i not in s:
        s.append(i)
if len(s)!=0 :
    print("{:.2f}".format((sum(s))/len(s)))
else:
    print("-1")