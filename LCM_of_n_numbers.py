def gcd(b,c):
    if c==0:
        return b
    return gcd(c,b%c)
n=int(input())
a=list(map(int,input().split()))
lcm=hcf=a[0]
for i in range(1,n):
    hcf=gcd(a[i],lcm)
    lcm=(a[i]*lcm//hcf)
print(lcm)