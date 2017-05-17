def func(): 
 a =12 
 print '''Inside the function the value of 
 a is acting as local variable''', a 
a= 10 
func() 
print '''Outside function the value of a is 
 acting as global variable''',a