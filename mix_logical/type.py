
'''fined the type'''

var=input("enter any data type:")
if type(eval(var))==str:
	print(var,"its a string data type")
elif type(eval(var))==int:
	print(var,"its a integer data type")
elif type(eval(var))==float:
	print(var,"its a float data type")
elif type(eval(var))==complex:
	print(var,"its a complex data type")
else:
	print(var,"its a bool data type")

