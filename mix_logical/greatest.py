# print greatest number 


num=int(input("enter any number:"))
num_1=int(input("enter any number:"))
num_2=int(input("enter any number:"))
if num>num_1 and num<num_2:
	print("second largest number",num)
elif num_1>num and num_1<num_2:
	print("second largest number",num_1)
elif num_2>num and num_2<num_1:
	print("second largest number",num_2)
elif num<num_1 and num>num_2:
	print("second largest number",num)
elif num_1<num and num_1>num_2:
	print("second largest number",num_1)
elif num_2<num and num_2>num_1:
	print("second largest number",num_2)
else:
	print("rest of the code") 



num=int(input("enter any number:"))
num_1=int(input("enter any number:"))
num_2=int(input("enter any number:"))
if num>num_1 and num>num_2:
	if num_1<num and num_1>num_2:
		print("greatest",num ,"second greatest",num_1)
	else:
		print("going to check next 1")
if num_1>num and num_1>num_2:
	if num_2>num and num_2<num_1:
		print("greatest,",num_1 ,"second greatest",num_2)
	else:
		print("going to check next 2")
if num_2>num and num_2>num_1:
	if num>num_1 and num<num_2:
		print("greatest",num_2 ,"second greatest",num)
	else:
		print("going to check next 3")
if num<num_1 and num>num_2:
	if num_1>num_2 and num_1>num:
		print("greatest",num_1, "second greatest",num)
	else:
		print("going to	check next 4")
if num<num_1 and num_2>num_1:
	if num_1>num and num_2>num:
		print("greatest",num_2,"second greatest",num_1)
	else:
		print("going to check next 5")
if num>num_1 and num>num_2:
	if num_2>num_1:
		print("greatest",num,"second greatest",num_2) 
	else:
		print("going to check next 6")
else:
	print`
	("rest of the code")




