##print(averege number):
i=1
sum=0
while i<=5:
	n=int(input("number:"))
	sum=sum+n
	print(sum)
	averege=sum/5
	i=i+1
if averege%5==0:
	print ("divisible")
else:
	print ("nahi hai")
print(averege)


#(average formula)
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
average=(num1+num2+num3)/3
print("average =" ,average)