age = int(input("Enter age:"))
sex = input("Enter sex:")
status = input("Enter marital_status:,yes/No:")
if (sex == "female"):
    print("she will work only urban areas")
if (sex == "male"):
 	if (age >= 20 and age < 40):
 		print("He will work anywhere") 
if (sex == "male"):
 	if (age >= 40 and age <= 60):         
 		print("He can work in urban areas only")
else:
	print("ERROR")
