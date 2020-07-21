
'''shasha Traveise Pvt.Ltd Gives the following discount to its customers 
Ticket amount 					Discount
Above Rs 70000					18%
Rs 55001 to Rs 70000            16%
Rs 35001 to Rs 55000			12%
Rs 25001 to Rs 35000   			10%
Less then Rs 25001   			2%'''

sl=int(input("Enter the sl.no:"))
Name=input("Enter the Name:")
ticket_amount=int(input("enter the price:"))
if ticket_amount>70000:
	Discount=ticket_amount*18/100
	total_amount=ticket_amount-Discount
	print("sl,No=",sl, "Name=",Name,"Discount=",Discount,"Net_amount=",total_amount)
elif ticket_amount>=55001 and ticket_amount<=70000:
	Discount=ticket_amount*16/100
	total_amount=ticket_amount-Discount
	print("sl,No=",sl,"Name=",Name,"Discount",Discount,"Net_amount",total_amount)
elif ticket_amount>=35001 and ticket_amount<=55000:
	Discount=ticket_amount*12/100
	total_amount=ticket_amount-Discount
	print("sl,No=",sl,"Name=",Name,"Discount",Discount,"Net_amount",total_amount)
elif ticket_amount>=25001 and ticket_amount<=35000:
	Discount=ticket_amount*10/100
	total_amount=ticket_amount-Discount
	print("sl,No=",sl,"Name=",Name,"Discount",Discount,"Net_amount",total_amount)
else ticket_amount<25001:
	Discount=ticket_amount*2/100
	total_amount=ticket_amount-Discount
	print("sl,No=",sl,"Name=",Name,"Discount",Discount,"Net_amount",total_amount)
