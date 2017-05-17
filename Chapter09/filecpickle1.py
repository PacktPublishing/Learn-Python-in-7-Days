import cPickle as pickle
name = ["mohit","bhaskar", "manish"]
skill = ["Python", "Python", "Java"]
pickle_file = open("emp1.dat","w") 
pickle.dump(name,pickle_file) 
pickle.dump(skill,pickle_file)
pickle_file.close()