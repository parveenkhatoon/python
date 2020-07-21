#pattern
'''
	*
   * *
  * * *
 * * * *
* * * * *'''
num=5
i=0
while i<num:
	j=4-i
	while j>0:
		print(end=" ")
		j-=1
	n=i
	while n>0:
		print("*",end=" ")
		n-=1
	print()
	i+=1

# num=0
# i=5
# while i>num:
# 	j=1-i
# 	while j<=4:
# 		print(end=" ")
# 		j+=1
# 	n=0
# 	while n<i:
# 		print("*",end=" ")
# 		n+=1
# 	print()
# 	i-=1
