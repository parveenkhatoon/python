
age = int(input("Enter the age:"))
if age <= 2:
	print("person is baby")
if age > 2 and age < 4:
	print("person is a toddler")
if age >= 4 and age < 13:
	print("person is the kid")
if age >= 13 and age < 20:
	print("person is a teenager")
if age >= 20 and age < 65:
	print("person is an adult")
if age >= 65:
	print("person is an elder")