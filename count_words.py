import sys

def count_words(file_name, word):
	file = open(file_name, "r")
	counter = 0;
	for line in file:
		counter += line.count(word)
	return counter

if (len(sys.argv)) != 3:
	print ("2 arguments needed: file_name and word to count.")
else:
	file_name = sys.argv[1]
	word = sys.argv[2]
	result = count_words(file_name, word)
	print("There are " + str(result) + " words " + word + " in file " + file_name + ".\n")




