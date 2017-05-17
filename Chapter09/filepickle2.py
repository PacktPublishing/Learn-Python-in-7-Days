import pickle 
pickle_file = open("emp1.dat",'r') 
name_list = pickle.load(pickle_file) 
skill_list =pickle.load(pickle_file) 
print name_list ,"\n", skill_list 