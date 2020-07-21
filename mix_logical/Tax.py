'''# To foster a sense of water department has an annual water 
# conservation tax policy.The rates are based on the water consumtion 
# of the consumer.
# Tax Rate in Rs						water consumed(in Gallons)
# 475.00					more than 45 but 75 or less
# 750.00						more than 75 but 125 or less
# 1225.00						more than 125 but 200 or less
# 1650.00						more than 200 but 350 or less
# 2000.00						more than 350''' 

gallons=int(input("Enter the gallons:"))
if gallons>=45 and gallons<75:
	tax=gallons*475.00
	totaltax=gallons+tax
	print("total_tax;",totaltax)
elif gallons>=75 and gallons<125:
	tax=gallons*750.00
	totaltax=gallons+tax
	print("total_tax;",totaltax)
elif  gallons>=125 and gallons<200:
	tax=gallons*1225.00
	totaltax=gallons+tax
	print("total_tax;",totaltax)
elif gallons>=200 and gallons<350:
	tax=gallons*1650.00
	totaltax=gallons+tax
	print("total_tax;",totaltax)
else gallons>350:
	tax=gallons*2000.00
	totaltax=gallons+tax
	print("total_tax;",totaltax)	


gallons=int(input("Enter the gallons:"))
if gallons>=45 and gallons<75:
	print("total_tax; 475.00")
elif gallons>=75 and gallons<125:
	print("total_tax; 750.00")
elif  gallons>=125 and gallons<200:
	print("total_tax; 1225.00")
elif gallons>=200 and gallons<350:
	print("total_tax;1650.00")
elif gallons>350:
	print("total_tax; 2000.00")
else gallons<45:
	print("total_tax;Nothing")