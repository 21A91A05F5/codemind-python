a=input()
b=input()
a=a.lower()
b=b.lower()
if len(a)==len(b) :
    if(sorted(a)==sorted(b)):
        print(True)
    else:
        print(False)
else:
    print(False)