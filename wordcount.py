# # put your code here.

import sys

def word_counter(file_name):
	""" Counts words in document. """

	word_dict = {}
	try :
		poem_data = open(file_name)
	except:
		print "Not a valid file."
		sys.exit(1)
	for line in poem_data:
		line = line.rstrip()
		line = line.lower()
		poem_line = line.split()
		for item in poem_line:
			item = item.strip("\".,!?-:;_\'")
			word_dict[item] = word_dict.get(item, 0) + 1
	for word, word_count in word_dict.iteritems():
		print "{} {}".format(word, word_count)
	poem_data.close()

word_counter(sys.argv[1])
