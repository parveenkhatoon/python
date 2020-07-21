'''Remove Substring
Aapko aisa program likhna hai, jo subStr ki saari occurences 
ko mainStr se hata degi. Yaani uppar wale program ka output yeh hoga:
mainStr mei subStr ko replacementStr se replace kar kar print karo.'''

mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr="over"
sub="no"
my_list=mainStr.split()
index=0
while index<len(my_list):
	if my_list[index]==subStr:
		my_list.remove(subStr)
		my_list.insert(5,sub)
		my_list.insert(13,sub)
		break
	index+=1
print(my_list)

	




	


