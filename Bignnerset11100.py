def proddig():
	n=int(input())
	p=1
	while(N!=0):
		r=N%10
		p=p*r
		N//=10
	print(p)
try:
	proddig()
except:
	print('invalid')
