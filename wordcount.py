# put your code here.

def word_counter(file_name):
	""" Counts words in document. """

	word_dict = {}
	poem_data = open(file_name)
	for line in poem_data:
		line = line.rstrip()
		poem_line = line.split(" ")
		for item in poem_line:
			word_dict[item] = word_dict.get(item, 0) + 1
	for word, word_count in word_dict.iteritems():
		print "{} {}".format(word, word_count)
	poem_data.close()

word_counter("test.txt")
