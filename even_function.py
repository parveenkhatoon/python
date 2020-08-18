def check_numbers():
    num=int(input("Enter the number:"))
    num1=int(input("Enter the number:"))
    if num%2==0 and num1%2==0:
        print("dono number even hai")
    else:
        print("dono number even nhi hai")
check_numbers()

def check_number_list():
    list1=[2,6,18,10,3,75]
    list2=[6,19,24,12,3,87]
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("Dono number even hai")
        else:
            print("Dono number even nhi hai")
        i+=1
check_number_list()
