from collections import defaultdict
game = defaultdict(lambda : "Cricket")

game["A"]= "Football"
game["B"] = "Badminton"

print game 
print game["A"]
print game["B"]
print game["C"]