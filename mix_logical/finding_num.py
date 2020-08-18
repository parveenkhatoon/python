num=1253
for i in range(num):
	if num%2==0 and num==3:
		print("yes")
	else:
		print("no")


'''check its 3 is their are not '''

num=int(input("enter the number:"))
if num%10==3:
	if num%2==0:
		print("yes")
	else:
		print("no")
else:
	print("in num their is 3 but not divisible by 2")