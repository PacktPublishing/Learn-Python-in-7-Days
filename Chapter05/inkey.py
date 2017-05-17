port1 = {21: "FTP", 22 :"SSH", 23: "telnet", 80: "http"}
key = int(raw_input("Enter the key "))
if key in port1:
	print "YES"
else :
	print "NO"