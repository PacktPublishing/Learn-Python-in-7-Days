import pickle 
pickle_file = open("emp2.dat",'r') 
all_data = pickle.load(pickle_file) 
print all_data["skill"]
print all_data["name"]
