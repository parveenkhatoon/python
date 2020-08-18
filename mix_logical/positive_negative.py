'''Take a number and check wherther it is 
is positive ,negative or a zero'''

x=int(input("enter the number:"))
if x==0:
	print("its zero")
elif x>0:
	print("positive number")
else x<0:
	print("nagetive number"_)


num=int(input("enetr number:"))
num1=int(input("enter number:"))
if num<num1:
	start=num 
	second=num1
else:
	start=num1
	second=num
while start<=second:
	if start<=-1 and start>=-10:
		print(start)
	if start>=1 and start<=10:
		print(-start)
	start+=1


