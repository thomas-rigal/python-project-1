user_sentence = raw_input('Enter a sentence with 10 or more words, please:')

for letters in user_sentence.split():
	if len(letters)%2 == 0:
		print letters