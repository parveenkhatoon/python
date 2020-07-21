
##print(gussin number):
i=1
n=5
while i<=5:
	x=int(input("number:"))
	if x==n:
		print("win")
		break
	i=i+1
if x!=n:
    print("lose")



##print(gussing with sume comment):
i=1
n=5
while i<=5:
    x=int(input("Enter number:"))	
    if x==n:
        print("win")
        break
    if x<n:
	    print("apka number chota hai! ek bar or try kro")
    if x>n:
        print("apka number bada hai! ek bar or try kro")
    i=i=1
