def ispalindrome(num):
    m=num
    rn=0
    while(num):
        d=num%10
        num=num//10
        rn=rn*10+d
    if rn==m :
        return True
    else:
        return False
def clspalindrome(n):
    sp=n-1
    while(not(ispalindrome(sp))):
        sp-=1
    lp=n+1
    while(not(ispalindrome(lp))):
        lp+=1
    if(abs(n-lp)>(abs(n-sp))):
        print(sp)
    elif(abs(n-lp)==(abs(n-sp))):
        print(sp,lp,end=' ')
    else:
        print(lp)
n=int(input())
clspalindrome(n)