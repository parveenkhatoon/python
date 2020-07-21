card=input("Enter the insert_card:")
if card=="insert":
		print("card is insert rigth select your language;")
		language=input("Enter the language:/english/hindi/")
		if language=="english" or language=="hindi":
			print("you select",language," language")
		else:
			print("choosa another language")
			bank=input("Enter the bank_name:/SBI/pnb/icci/")
			if bank=="SBI" or bank=="pnb" or bank=="icci":
				print("your selected bank",bank,"this; Enter your ATM_PIN number")
				ATM_PIN=int(input("Enter tha ATM_PIN:"))
				if ATM_PIN==9958:
					print("PIN is rigt:How much amount you want to withrawal Enter the amount")
					amount=int(input("Enter the amount:"))
					balance=10000
					if amount<=balance:
						amount=balance-amount
						print("your amount balance is under tha your balance you are secsess to withrawal your amount: ","now this much amount",amount,"you have")
						card1=input("Enter tha position:/logout:")
						if card1=="logout":
							print("Thanku for using this ATM")
						else:
							print("logout properl")
					else:
						print("this amount out of your bank corrent amount:",amount)
				else:
					print("PIN is wrong")
			else:
				print("this branch is not in this ATM")
else:
	print("your card is not insert properly please tyr agine;")