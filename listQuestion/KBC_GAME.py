
Question_list=[
	"how many continates are there?",
	"what is capital of india?",
	"Ng me kon sa cours hota hai?",
]

option_list=[["nine","seven","one","eigth"],
		["gujrat","bhopal","delhi","banglore"],
		["jhadu pocha","khana pakana","softwere engnareeing","palgpan"]
]

solution_list=[2,3,3]

index=0
while index<len(Question_list):
	print("Apka sawal hai!!")
	print("")
	print(Question_list[index])
	j=0
	print("Apka options hai!!")
	while j<len(option_list[index]):
		print(j+1,option_list[index][j])
		j=j+1
	answer=int(input("Enter your option_list ka answer:"))
	if answer==solution_list[index]:
		print("congrats!! your answer is right")
	else:
		print("opps!!! sorry your answer is wrong")
	index=index+1
print("game is over!! thanku for playing the game")	



Question_list=["how many continates are there?",
                "what is capital of india?",
                "Ng me kon sa cours hota hai?",]

option_list=[["nine","seven","one","eigth"],
            ["gujrat","bhopal","delhi","banglore"],
            ["jhadu pocha","khana pakana","software engineer","palgpan"]]

solution_list=[2,3,3]

index=0
hint_list=[[0,2],[3,2],[3,1]]
while index<len(Question_list):
	print("apka Question hai !!")
	print("")
	print(Question_list[index])
	j=0
	print("Apka options hai")
	while j<len(option_list)+1:
	    print(j+1,option_list[index][j])
	    j+=1
	answer=int(input("Enter the answer/you have 5050 options also:-"))
	if answer==solution_list[index]:
		print("congrets your answer is right!!")
		if user==solution_list[index]:
			print("your answer is right")
		else:
			print("your answer is wrong")
	else:
		print("opps sorry wrong answer")
	index+=1
print("Thanku for playing KBC game")















