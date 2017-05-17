class MyException(Exception): 
	def __init__(self, value):
		self.value = value 
	def __str__(self):
		return (self.value) 
try: 	
	num = raw_input("Enter the number : ")
	if num == '2':
		raise MyException("ohh") 
	else :
		print "number is not 2"
except IOError: 
	print "My exception occurred" 