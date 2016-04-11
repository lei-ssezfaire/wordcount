# put your code here.

def word_counter(file_name):
	word_dict = {}
	poem_data = open(file_name)
	for line in poem_data:
		line = line.rstrip()
		poem_line = line.split(" ")
		for item in poem_line:
			if item in word_dict:
				word_dict[item] = word_dict[item] + 1
			else:
				word_dict[item] = 1
	for word, word_count in word_dict.items():
		print "{} {}".format(word, word_count)
	poem_data.close()
word_counter("test.txt")
