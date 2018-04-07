words=['hangman']
guessWord=words
hidden=['_']*len(guessWord)
turnsLeft=5;






	print 'Welcome to Hangman! \n'

	while (turnleft>0):
		guess= raw_input('Enter your guess\n')

		if(guess is in guessWord):
			print 'you got one'
			
