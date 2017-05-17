from collections import defaultdict

def func():
	return "Cricket"

game = defaultdict(func)

game["A"]= "Football"
game["B"] = "Badminton"

print game 
print game["A"]
print game["B"]
print game["C"]