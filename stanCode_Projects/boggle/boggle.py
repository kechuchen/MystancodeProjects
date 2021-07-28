"""
File: boggle.py
Name: kechu
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DICT = []
DIRECTION = [(-1, -1), (0, -1),
			  (1, -1), (-1, 0),
			 (1, 0), (-1, 1),
			 (0, 1), (1, 1)]
answers = []
def main():
	"""
	TODO:
	"""
	start = time.time()
	read_dictionary()
	boggle = []
	pass_info = [[0, 0, 0, 0],
				 [0, 0, 0, 0],
				 [0, 0, 0, 0],
				 [0, 0, 0, 0]
				 ]

	for i in range(4):
		print(i+1, end="")
		data = input(" row of letters: ")
		data = data.split()
		boggle.append(data)

	for x in range(4):
		for y in range(4):
			helper(boggle, pass_info, x, y, word='')

	print('There are ', len(answers), ' words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dic_list = line.split()
			for word in dic_list:
				DICT.append(word)

def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for w in DICT:
		if w.startswith(sub_s):
			return True
	return False


def valid(i, j, passed):
	"""
	to check whether the index is in the range and whether we have pass an element of certain index.
	"""
	return (0 <= i < 4) and (0 <= j < 4) and not passed[i][j]


def helper(boggle, pass_info, x, y, word=''):
	# Base Case

	if len(word) >= 4 and word in DICT and word not in answers:
		answers.append(word)
		print('Found', word)

	# choose
	pass_info[x][y] = 1
	word += boggle[x][y]

	# loop over neighbors
	for direct in DIRECTION:
		if has_prefix(word):
			i, j = direct
			nx, ny = x+i, y+j
			if valid(nx, ny, pass_info):
				helper(boggle, pass_info, nx, ny, word)  # explore

	# un-choose (backtrack)
	pass_info[x][y] = 0

if __name__ == '__main__':
	main()
