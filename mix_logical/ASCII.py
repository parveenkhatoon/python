'''Check whether a entered charachter is lowercase (a to z) or
uppercase (A to Z)'''

letter=input("enter any kye:")
if ord(letter)>=0 and ord(letter)<=47:
	print("its a symbol "+(letter))
elif ord(letter)>=48 and ord(letter)<=57:
	print("its a counting "+(letter))
elif ord(letter)>=58 and ord(letter)<=64:
	print("its a special charachter "+(letter))
elif ord(letter)>=91 and ord(letter)<=96:
	print("its a special charachter "+(letter))                                                           
elif ord(letter)>=65 and ord(letter)<=90:
	print("word is capital "+(letter))
elif ord(letter)>=91 and ord(letter)<=96:
	print("its a symbol "+(letter))
elif ord(letter)>=97 and ord(letter)<=122:
	print("word is small "+(letter))
elif ord(letter)>=123 and ord(letter)<=127:
	print("its a symbol "+(letter))
else:
	print("nothing")





