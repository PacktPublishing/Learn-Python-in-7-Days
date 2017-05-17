list1 = [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)]

def sum1(tup1):
	a,b = tup1
	c = a+b
	return c

list1.sort(key=sum1)
print list1
	