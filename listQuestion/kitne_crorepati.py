'''Kitne Crorepati?
Aapko ek aisa program likhna hai jo, bataye, ki uppar wali list mei kitne log:

1 - Crorepati hai
2 - Lakhpati hai
3 - Dilwale

Jinke paas 1 crore ya usse jyada paisa hai, woh crorepati hai.
Jinke paas 1 lakh ya usse jyada paise hai, woh lakhpati hai.
Baaki sab Dilwale hai.'''

list1= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
index=0
crorepati=0
lakhpati=0
Dilwale=0
while index<len(list1):
	if list1[index]>=10000000:
		print("crorepati hai")
		crorepati=crorepati+1
	elif list1[index]>=100000:
		print("lakhpati hai")
		lakhpati=lakhpati+1
	else:
		print("Dilwale hai")
		Dilwale=Dilwale+1
	index+=1
print("crorepati are",crorepati)
print("lakhpati are",lakhpati)
print("Dilwale are",Dilwale)