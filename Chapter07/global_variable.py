def func(): 
   global k 
   k=k+7 
   print "variable k is now global",k 
k=10
func()
print "Accessing the value of k outside the function",k