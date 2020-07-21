''' A shop will give discount of 10% if the cost of 
purchased quantity is more than 1000'''

quantity=int(input("enter tha quantity:"))
purchased=int(input("enter the purchased:"))
if purchased>1000:
	Discount=purchased*10/100
	total_purchased=purchased-Discount
	print("with bonas",(total_purchased))
else:
	print("no bonas",(purchased))
