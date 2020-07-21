'''electronics shop has announced the following seasonal
 discounts on the purchase of certain items
Discount on				  Discount on
Discount PC					laptop
	5.0%						0.0%
	7.5%						5.0%
	10.0%						7.5%
	15.0%						10.0% '''
thing=input("Enter the thing:")
purchase_amount=int(input("Enter the amount:"))
if thing=="laptop":
	if  purchase_amount>0 and purchase_amount<=25000:
		Discount=purchase_amount/100*0.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
	elif purchase_amount>=25001 and purchase_amount<=57000:
		Discount=purchase_amount/100*5.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)	
	elif purchase_amount>57000 and purchase_amount<=100000:
		Discount=purchase_amount/100*7.5
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
	elif purchase_amount>100000:
		Discount=purchase_amount/100*10.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
elif thing=="Desktop":
	if purchase_amount>0 and purchase_amount<=25000:
		Discount=purchase_amount/100*5.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
	elif purchase_amount>=25001 and purchase_amount<=57000:
		Discount=purchase_amount/100*7.5
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
	elif purchase_amount>57000 and purchase_amount<=100000:
		Discount=purchase_amount/100*10.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)
	elif purchase_amount>100000:
		Discount=purchase_amount/100*15.0
		Net_amount=purchase_amount-Discount
		print("Net_amount=",Net_amount,"Discount",Discount,)


