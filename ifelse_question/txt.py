txt = ("python is a powerful and easy")
file_name = input("Enter the word:")
app = file_name.endswith('.txt')
if app:
	print ("ok")
else:
	print("invalid file type")
