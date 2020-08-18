''' A shop will give discount of 10% if the cost of 
purchased quantity is more than 1000'''

salary=int(input("enter tha selery:"))
year=int(input("enter the year:"))
if year>5:
	bonus=salary*5/100
	total_salary=salary+bonus
	print("with bonus",total_salary)
else:
	print("no bonus",salary)

''' in this question we have to print if year is 5 than bonus also 5% if 
year is 20 bonus also 20%'''

salary=int(input("enter the salary:"))
year=int(input("enter the year:"))
if year>=1:
	bonus=salary*year/100
	total_salary=salary+bonus
	print("salary with bonus:",total_salary)
else:
	print("no bonus",salary)


'''if saalry is 1 year so print 5% bonus if year is 2 print 10% 
bonus and  if year is 10 than print 100% bonus'''


salary=int(input("enter the salary:"))
year=int(input("enter the year:"))
if year>=1:
	bonus=salary*(year*5)/100
	total_salary=salary+bonus
	print("salary with bonus:",total_salary)
else:
	print("no bonus",salary)













