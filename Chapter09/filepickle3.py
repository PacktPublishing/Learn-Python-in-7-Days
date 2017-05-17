import pickle 
pickle_file = open("emp2.dat",'w') 
leapx_team = {
		'name' : ["Mohit", "Ravender", "Himmat", "Robbin"],
		'skill' : ["Python","Data Analytic", "Information Security", "SAP"]
		} 
pickle.dump(leapx_team,pickle_file) 
pickle_file.close()