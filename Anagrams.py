s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=list(s1)
s2=list(s2)
s1.sort()
s2.sort()
if s1==s2 :
    print(True)
else:
    print(False)