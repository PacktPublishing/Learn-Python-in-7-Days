from collections import defaultdict

game = defaultdict(list)

tuple_list_county =  [('US', 'Visconsin'), ('Germany', 'Bavaria'), ('UK', 'Bradfordshire'), ('India', 'punjab'), ('China', 'Shandong'), ('Canada', 'Nova Scotia')]
	
print game["any_value"]  

for k,v in tuple_list_county:
	game[k].append(v)

print game