def divide1():
	try:
		num = int(raw_input("Enter the number "))
		c = 45/num
		print c 
	except ValueError : 
		print "Value is not int type" 
	except ZeroDivisionError : 
		print "Don't use zero" 
	else: 
		print "result is ",c
		
divide1()	