def reverse(n):
    r=0
    while n:
        r=r*10+n%10
        n//=10
    return r
    
n = int(input())
while n:
        n+=reverse(n)
        if reverse(n)==n :
            print(n)
            break