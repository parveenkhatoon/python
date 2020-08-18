'''debuging'''
'''def voter(age):
if age < 18:
	print("eligible")
else:
	print("not eligible")
	voter(20)'''

def voter(age):
    if age<18:
	    return("eligible")
    else:
	    return("not eligible")
print(voter(20))