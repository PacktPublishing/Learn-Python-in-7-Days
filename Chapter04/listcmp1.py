list1 = [10,9,3,7,2,1,23,1,561,1,1,96,1]

def cmp1(x,y):
	
	if x == 1 or y==1:
		c = y-x
	else:
		c = x-y
	return c
		
list1.sort(cmp = cmp1)

print list1