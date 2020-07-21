i=1
while i<=5:
	player1=input("Enter tha opetion:")
	player2=input("Enter the opetion:")
	if player1=="paper" and player2=="stone":
		print("player1 is win")
	elif player1=="stone" and player2=="scissors":
		print("player1 is win")
	elif player1=="scissors" and player2=="paper":
		print("player1 is win")
	else:
		print("player2 is win")
	i+=1
print("thanku for using this game")