
def kmp(pattern, text):
	""" 
	Use the knuth-morris-pratt algorithm to find the initial index of the 
	first occurrence of a pattern within the text. 
	(single pattern matching problem)

	Time: O(|text| + |pattern|) 

	Args:
		pattern: A string within text.
		text: A string containing pattern.

	Adapted from pseudocode at: 
	https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
	"""

	if len(pattern) < 0 or len(text) < 0 or len(pattern) > len(text):
		raise Exception('Illegal Arguments')

	table = _preprocessing(pattern)

	text_i = 0
	pattern_i = 0

	while text_i + pattern_i < len(text):
		if pattern[pattern_i] == text[text_i + pattern_i]:
			if pattern_i == len(pattern) - 1:
				return text_i
			else:
				pattern_i += 1
		else:
			if pattern_i > 0:
				text_i = text_i + pattern_i - table[pattern_i]
				pattern_i = table[pattern_i]
			else:
				text_i += 1
				pattern_i = 0

	return None

def _preprocessing(pattern):

	if len(pattern) < 0:
		raise Exception('Illegal Arguments')

	table = [0 for _ in range(len(pattern))]

	table_i = 2
	next_char_i = 0

	table[0] = -1
	table[1] = 0

	while table_i < len(pattern):
		if pattern[table_i - 1] == pattern[next_char_i]:
			table[table_i] = next_char_i + 1
			next_char_i += 1
			table_i += 1
		elif next_char_i > 0:
			next_char_i = table[next_char_i]
		else:
			table[table_i] = 0
			table_i += 1

	return table

	