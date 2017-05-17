from collections import defaultdict

game = defaultdict(int)

list1 = ['cricket', 'badminton', 'hockey' 'rugby', 'golf', 'baseball' ,   'football']

for each in list1:
	game[each]= game[each]+1
	
print game