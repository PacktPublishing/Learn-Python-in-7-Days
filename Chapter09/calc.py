
def sum1(a,b):
	try:
		c = a+b
		return c
	except :
		print "Error in sum1 function"

def divide(a,b):
	try:
		c = a/b
		return c
	except :
		print "Error in divide function"
print divide(10,0)
print sum1(10,0)