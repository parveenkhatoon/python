
def numbers_less_than_twenty(num_list):
  index = 0
  num_list_sub_20=[]
  while index < len(num_list):
    if num_list[index] < 20:
      num_list_sub_20.append(num_list[index])
    index+=1
  return(num_list_sub_20)
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)
print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
