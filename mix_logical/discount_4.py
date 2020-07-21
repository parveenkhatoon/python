'''a cloth showroom has announced the following  festival discount on the purchase 
of items.based on the total cost of the items purchased
Total cost						Discount(in percentage)
Less than Rs 2000				5%
Rs 2001 to Rs 5000				25%
Rs 5001 to Rs 10000				35%
Above Rs 10000					50%'''


fastival=input("Enter any fastival:")
purchase=int(input("purchase_amount:"))
if purchase<2000:
	Discount=purchase*5/100
	total_amount=purchase-Discount
	print("total_amount=",total_amount)
elif purchase>=2001 and purchase<=5000:
	Discount=purchase*25/100
	total_amount=purchase-Discount
	print("total_amount=",total_amount)
elif purchase>=5001 and purchase<=10000:
	Discount=purchase*35/100
	total_amount=purchase-Discount
	print("total_amount=",total_amount)
else purchase>10000: 
	Discount=purchase*50/100
	total_amount=purchase-Discount
	print("total_amount=",total_amount)

