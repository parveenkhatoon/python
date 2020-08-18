banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file = open("people1-exercise.txt","w")
for i in range(0,len(banks_list)):
    file_write = my_file.write(banks_list[i]+"\n")
    print()
print(file_write)
