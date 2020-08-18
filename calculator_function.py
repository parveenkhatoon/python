
'''with using input'''
# def calculator():
#     num=int(input("Enter the number:"))
#     num1=int(input("Enter the number:"))
#     symbol=input("Enter the symbol:")
#     if symbol=="+":
#         print(num + num1)
#     elif symbol=="-":
#         print(num - num1)
#     elif symbol=="/":
#         print(num / num1) 
#     elif symbol=="*":
#         print(num * num1)
#     elif symbol=="%":
#         print(num % num1)
#     else:
#         print("Rest of the code")
# calculator() 


'''using list calculator '''
def list_change():
    list1=[5,10,15,20]
    list2=[2,20,3,5]
    symbol=input("Enter the symbol:")
    i=0
    my_list=[]
    while i<len(list1):
        if symbol=="*":
            sum=(list1[i]*list2[i])
            my_list.append(sum)
        elif symbol=="-":
            sum=(list1[i]-list2[i])
            my_list.append(sum)
        elif symbol=="/":
            sum=(list1[i]/list2[i])
            my_list.append(sum)
        elif symbol=="+":
            sum=(list1[i]+list2[i])
            my_list.append(sum)
        elif symbol=="%":
            sum=(list1[i]%list2[i])
            my_list.append(sum)
        i+=1
    print(my_list)
list_change()
















