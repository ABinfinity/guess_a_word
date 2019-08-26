from os import system
import time
import sys
import random

def intro():
	name = input("What is your name? ")
	print("Hello, " + name, "time to play GUESS-A-WORD!")
	print()
	time.sleep(1)
	print("Loading...")
	time.sleep(1.5)
	system('clear')
	print("<---Welcome to GUESS-A-WORD--->")
	print()
	time.sleep(1.5)
	print("Rules-->")
	print("1. Guess the word")
	print("2. 10 wrong guesses and game over")
	time.sleep(1.5)


def fails(turns):
	turns -=1
	print("Wrong")
	print("You have", + turns, 'lives')
	if turns == 0:           
		print ("You Loose" )
	
	return turns


def success(turns):
	print("Right")
	print("You have", + turns, 'lives')



def word_format(char_left, word, guesses):
	# for every character in secret_word    
	for char in word:
	# see if the character is in the players guess
		if char in guesses:    
			print(char, end = " "),    
		else:
			print ("_", end = " "),     
	   
			# count unfilled letters in word left
			char_left += 1   
	return char_left

def word_list():
	words = ["appreciate","accuse","applause","ballet","bullet","badass","convention","competition","complementary","donation","destruction","displacement","eulogy","emails","entertainment","fascination","formation","forming","geology","gallantry","government","hospital","harmony","honorable","important","inconsistent","inconvention","jackass","jolly","jumping","king","kernel","kite","lemon","limitation","lack","monotomy","minion","manipulation","nominee","null","nation","omnipotent","oscillate","overall","possible","placement","pavement","querry","queue","qualification","rescue","rectification","rally","salmon","somebody","sauce","television","teleport","temporary","usual","usefull","unusual","vermon","verdict","validation","workshop","worship","warfare","xylophone","xray"]
	return random.choice(words)


if __name__ == '__main__':
	intro()
	want = input("Continue..?(y/n)")
	print(want.lower())
	if want.lower() == "n":
		sys.exit()

	system("clear")
	word = word_list()
	guesses = ''
	turns = 10
	print(" _" * len(word))

	while turns > 0:         

		char_left = 0             
		print()
		guess = input("guess a character:")
		system('clear') 
		guesses += guess.lower()                    
	 
		if guess.lower() not in word:  
			turns = fails(turns)        
			
		
		else:
			success(turns)
		
		char_left = word_format(char_left, word, guesses)

		 

		# print You Won
		if char_left == 0:
			print()       
			print("You won!!!")
			break              

		