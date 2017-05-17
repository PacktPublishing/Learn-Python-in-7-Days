try: 
	num = int(raw_input("Enter the number ")) 
	re = 100/num 
except: 
	print "Something is wrong" 
else: 
	print "result is ",re 
finally : 
	print "finally program ends" 