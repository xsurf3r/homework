# import random module
import random

# Print multiline instruction
# veikt virknes savienošanu
print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	# ņemt ievadi no lietotāja
	choice = int(input("User turn: "))

	# vai ir īssavienojuma operators
    # ja kāds no nosacījumiem ir patiess
    #, tad tas atgriež patieso vērtību
	
	# cilpa, līdz lietotājs ievada nederīgu ievadi
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	# inicializēt mainīgā choice_name vērtību
	# kas atbilst izvēles vērtībai
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	# print user choice
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	# Dators jauktajā secībā izvēlas jebkuru skaitli
	# among 1 , 2 and 3. lieto randint metodi
	# jaukatais modulis
	comp_choice = random.randint(1, 3)
	
    #cilpa līdz comp_choice vērtībai
    # ir vienāds ar izvēles vērtību
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# inicializēt comp_choice_name vērtību
    # mainīgais, kas atbilst izvēles vērtībai
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	# nosacījums laimestu
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	# drukā uzvarētāju
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("Do you want to play again? (Y/N)")
	ans = input()


	# if user input n or N then condition is True
	if ans == 'n' or ans == 'N':
		break
	
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
