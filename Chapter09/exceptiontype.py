try: 
	num = int(raw_input("Enter the number ")) 
	re = 100/num 
	print re
except Exception as e : 
	print e, type(e)
