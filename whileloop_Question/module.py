##print(i divisible by 3 print (Nav),i divisible by 7 print(gurukul),if i divisible by both print(Navgurukul)):
i=1
while i<=100:
	print(i)
	if i%3==0:
		print("Nav")
		if i%7==0:
			print("gurukul")
			if i%3==0 and i%7==0:
				print("navgurukul")
	i=i+1
