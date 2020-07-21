'''
Ek code likho jo kisi bhi list ke liye yeh output
karta hai, ki uss list mei odd numbers,
even numbers aur sab numbers ka:

count
sum
average'''

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
odd=0
even=0
sum=0
average=0
while index<len(elements):
	if elements[index]%2==0:
		print("elements is a even",elements[index])
		even=even+1
	else:
		print("elements are odd",elements[index])
		odd=odd+1
	sum=sum+elements[index]
	average=sum/elements[index]
	index=index+1
print("total even are",even)
print("total odd are",odd)
print(sum)
print(average)
