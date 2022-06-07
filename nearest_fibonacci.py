def nearestFibonacci(num):
	if (num == 0):
		print(0)
	a=0
	b=1
	c=a+b
	while (c<=num) :
		a=b
		b=c
		c=a+b
	if (abs(c-num)>abs(b-num)):
		k=b
	elif (abs(c-num)==abs(b-num)):
		    print(b,c,end=' ')
	else:
		k=c
	print(k)
N=int(input())
nearestFibonacci(N)

