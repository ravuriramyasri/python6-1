N=input()
list=[]
for i in range(0,N):
	int_input=int(raw_input())
	list.append(int_input)
for a in list:
	a=min(list)
print(a)
