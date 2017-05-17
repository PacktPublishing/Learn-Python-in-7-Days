def add1(x,y):
	
	if x>10 or y>10:
		c = 1 
	else :
		c = x-y
	return c
	
list_tup = [9,12,90,3,9,1,7,1,2,8,1,1,96,1]
list_tup.sort(cmp=add1)
print list_tup