my_file = open("people1-exercise.txt")
count=0
file_data = my_file.read()
list1 = file_data.split("\n")
for i in list1:
    if i:
        count=count+1
print("this is the people1-exercise.txt file total count = ",count)
