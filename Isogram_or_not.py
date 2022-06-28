s=input()
a=[]
for i in s:
    if s.count(i)>1 :
        break
    else:
        a.append(i)
if len(a)==len(s) :
    print(True)
else:
    print(False)