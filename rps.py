import random
amt = 50
ans = 'y'
options = ["r", "p", "s"]
wins = 0
losses = 0
ties = 0
print('You have $'+str(amt))
while amt >= 10 and ans == 'y':
	choice = input('Choose r, s or p')
	compChoice = random.choice(options)
	if compChoice == choice:
		print('You tied with the computer!')
		ties+=1
	elif compChoice == 'r':
		if choice == 'p':
			print('You beat computer')
			wins+=1
		elif choice == 's':
			print('Computer beat you')
			losses+=1
			amt-=10
	elif compChoice == 'p':
		if choice == 's':
			print('you beat computer')
			wins+=1
		elif choice == 'r':
			print('Computer beat you')
			losses+=1
			amt-=10
	elif compChoice == 's':
		if choice == 'r':
			print('you beat computer')
			wins+=1
		elif choice == 'p':
			print('Computer beat you')
			losses+=1
			amt-=10
	print('------------------------')
	print('you have $'+str(amt))
	print('wins :',wins)
	print('losses :',losses)
	print('ties :',ties)
	print('------------------------')
	if amt == 0:
		print('You do not have enough money! You are done.')
	else:	
		ans = input('play again? y or n')
		print('you have $'+str(amt))
