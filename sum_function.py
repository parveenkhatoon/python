# def add_numbers(num1,num2):
#     print(num1 + num2)
# add_numbers(56,12)

def add_numbers_list():
    list1=[50, 60, 10]  
    list2=[10, 20, 13] 
    i=0
    while i<len(list1):
        j=0
        sum=0
        while j<len(list2):
            sum=list1[i]+list2[i]
            j+=1
        print(sum)
        i+=1
    
add_numbers_list()
