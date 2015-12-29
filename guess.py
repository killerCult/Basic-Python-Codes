'''
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, this program should print out how many guesses it took to get your number.
'''

# Killer_Cult

begin = 50            #Start with middle number between 1 and 100
flag = 0              #Indicate if correct guess or not
high = 100            #Default high, subject to change
low = 0               #Default low, subject to change
count = 0             #Count the number of guesses

while flag==0:
	count+=1	 
	print "Is the number", begin,"? (yes/no):"
	guess = raw_input()
	if guess=="yes":
		print "Correct Guess"
		print "Took", count, "tries" 
		flag = 1
	elif guess=="no":
		print "Wrong Guess"		
		print "Was the guess higher or lower? (higher/lower)"
		hl = raw_input()
		if hl=="higher":
			high = begin			
			begin = begin - ((high-low)/2)
		elif hl=="lower":
			low = begin
			begin = begin + ((high-low)/2) 		
		else:
			print "Invalid Input"
	else:
		print "Invalid Input"
	
