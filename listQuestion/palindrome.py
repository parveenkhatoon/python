# name=["n","i","t","i","n"]
# index=name[-1::-1]
# print(name)
# if name==index:
# 	print("list palindrome hai",index)
# else:
# 	print("list palindrome nhi hai")
	

# i=1
# while (i<=100):
# 	prime=int(input("enter your num:"))
# 	if (prime>1 and prime%prime==0):
# 		print("it is prime num:",prime)
# 	else:
# 		print("it is not a prime num:",prime)
# 	i=i+1


# num = int(input("enter your num:"))
# i = 0
# while (i<=num):
# 	if num%2==0 and num>i and num%num==0:
# 		print("it is prime:",num)
# 	else:
# 		print("it is not a prime:",num)
# 	i = i + 1

# num = int(input("enter your num:"))
# i = 1
# while (i<=num):
# 	if (num>1):
# 		if (num%2==1 and num%num==0):
# 			print("it is prime:",num)
# 	# if num:
# 	# 	print("it is not a prime",num)
# 	# i+=1
# 		else:
# 			print("it is not a prime:",num)
# 	i+=1


# num = int(input("enter your num:"))
# a = 0
# while (a<=1):
# 	if (num>1):
# 		i = 1
# 		while (i<=1):
# 			if (num%2==1 and num%num==0 and num%1==0):
# 				print("it is a prime:",num)
# 			else:
# 				print("it is not a prime:",num)
# 			i = i + 1
# 		a = a 

# prime = int(input("enter your num:"))
# if prime%2==1 and prime%prime==0:
# 	print("it is  a prime",prime)
# if prime%1==0:
# 	print("it is prime",prime)
# else:
# 	print("it is not a prime",prime)



# prime = int(input("enter your num:"))
# i = 1
# while (i<prime):
# 	if (prime>1):
# 		prime = True
# 		a = 2
# 		while (a<prime):
# 			if (prime%a==0 and  prime%i==0 and prime%prime==0):
# 				print ("it is prime:",prime)
# 			else:
# 				print("it is not a prime:",prime)
# 		# if prime:
# 			# print("it is prime")
# 		prime = False
# 		a = a + 1
# 	i = i + 1



num = int(input("enter your num"))
i = 1
while (num!=i):
	if (num%i==0 and num%num==0):
		print("it is prime",num)
	elif (num%2==0 and num%num==0 and num%1==0):
		print("it is not a prime",num)
	i = i + 1

















