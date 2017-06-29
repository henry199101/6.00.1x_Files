def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers, and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	"""
	Test Cases
	buildCoder(3)
	{'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
	buildCoder(9)
	{'A': 'J', 'C': 'L', 'B': 'K', 'E': 'N', 'D': 'M', 'G': 'P', 'F': 'O', 'I': 'R', 'H': 'Q', 'K': 'T', 'J': 'S', 'M': 'V', 'L': 'U', 'O': 'X', 'N': 'W', 'Q': 'Z', 'P': 'Y', 'S': 'B', 'R': 'A', 'U': 'D', 'T': 'C', 'W': 'F', 'V': 'E', 'Y': 'H', 'X': 'G', 'Z': 'I', 'a': 'j', 'c': 'l', 'b': 'k', 'e': 'n', 'd': 'm', 'g': 'p', 'f': 'o', 'i': 'r', 'h': 'q', 'k': 't', 'j': 's', 'm': 'v', 'l': 'u', 'o': 'x', 'n': 'w', 'q': 'z', 'p': 'y', 's': 'b', 'r': 'a', 'u': 'd', 't': 'c', 'w': 'f', 'v': 'e', 'y': 'h', 'x': 'g', 'z': 'i'}
	"""
	import string

	transfer_dict ={}

	keys = string.ascii_lowercase * 2 + string.ascii_uppercase * 2
	values = string.ascii_lowercase * 2 + string.ascii_uppercase * 2

	for key in keys:
		transfer_dict[key] = values[keys.index(key) + shift]
	return transfer_dict


def applyCoder(text, coder):
	"""
	Applies the coder to the text. Returns the encoded text.

	text: string
	coder: dict with mappings of characters to shifted characters
	returns: text after mapping coder chars to original text
	"""
	"""
	>>> applyCoder("Hello, world!", buildCoder(3))
	'Khoor, zruog!'
	>>> applyCoder("Khoor, zruog!", buildCoder(23))
	'Hello, world!'
	"""
	text_result = []
	for char in text:
		if coder.has_key(char): # 如果text中的字符char出现在字典中
			text_result.append(coder[char]) # 则将转换后的字符加入text_char
		else: # 如果text中的字符char 不 出现在字典中，如逗号、感叹号
			text_result.append(char) # 则将字符(如逗号、感叹号)直接加入text_char
	# print "\'" + "".join(text_result) + "\'"
	return "".join(text_result)
	
# applyCoder("Hello, world!", buildCoder(3))
# applyCoder("Khoor, zruog!", buildCoder(23))


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
	### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

# applyShift('This is a test.', 8)
# applyShift('Bpqa qa i bmab.', 18)


def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

wordList = "words.txt"
text = "story.txt"
	
def findBestShift(wordList, text):
	"""
	Finds a shift(移位) key that can decrypt the encoded text.
	找到可以解密编码文本的移位键。
	text: string
	returns: 0 <= int < 26
	"""
	# 1. Set the maximum number of real words found to 0.
	num_of_real_word = 0
	# 2. Set the best shift to 0.
	best_shift = 0
	word_count = 0
	# 3. For each possible shift from 0 to 26:
	for num in range(26):
		# 4. Shift the entire text by this shift.
		# applyShift(text, num)
		# 5. Split the text up into a list of the individual words.
		list_of_single_words = applyShift(text, num).split(' ')
		# 6. Count the number of valid words in this list.
		for l_s_word in list_of_single_words:
			if isWord(wordList, l_s_word):
				word_count += 1
		# 7. If this number of valid words is more than the largest number of real words found, then:
		if word_count > num_of_real_word:
			# 8. Record the number of valid words.
			num_of_real_word = word_count
			# 9. Set the best shift to the current shift.
			best_shift = num
		# 10. Increment the current possible shift by 1. Repeat the loop starting at line 3.
		else:
			best_shift += 1
	# 11. Return the best shift.
	return best_shift