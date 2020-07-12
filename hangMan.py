import random

def print_scaffold(guesses, wd): # prints the scaffold
    if (guesses == 0):
        print "_________"
		print "|	 |"
		print "|"
		print "|"
		print "|"
		print "|"
		print "|________"
	elif (guesses == 1):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|"
		print "|"
		print "|"
		print "|________"
	elif (guesses == 2):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|	 |"
		print "|	 |"
		print "|"
		print "|________"
	elif (guesses == 3):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|	\|"
		print "|	 |"
		print "|"
		print "|________"
	elif (guesses == 4):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|	\|/"
		print "|	 |"
		print "|"
		print "|________"
	elif (guesses == 5):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|	\|/"
		print "|	 |"
		print "|	/ "
		print "|________"
    elif (guesses == 6):
		print "_________"
		print "|	 |"
		print "|	 O"
		print "|	\|/"
		print "|	 |"
		print "|	/ \ "
		print "|________"
		print "\n"
		print "The word was %s." %wd
		print "\n"
		print "\nYOU LOSE! TRY AGAIN!"
		print "\nWould you like to play again, type 1 for yes or 2 for no?"
		again = str(raw_input("> "))
		gain = again.lower()
		if again == "1":
			hangMan()
		return
    
def selectWord():
	file = open('FREQ')
	words = file.readlines() 
	myword = 'a'
	while len(myword) < 4: 
    myword = random.choice(words)
  	myword = str(myword).strip('[]')
  	myword = str(myword).strip("''")
  	myword = str(myword).strip("\n")
  	myword = str(myword).strip("\r")
	myword = myword.lower()
	return myword

hangMan()