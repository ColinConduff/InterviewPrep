def is_anagram(s, t):
	""" 
	Return True if the second argument is an anagram 
	of the first argument.

	Time: O(|s| + |t|)
	Space: O(min(|s| + |t|))
	"""
	if len(t) < len(s):
		# swap to improve space complexity
		s, t = t, s

	s_dict = {}

	for letter in s:
		if letter in s_dict:
			s_dict[letter] += 1
		else:
			s_dict[letter] = 1

	for letter in t:
		if letter in s_dict:
			s_dict[letter] -= 1
			
			if s_dict[letter] == 0:
				del s_dict[letter]
		else:
			return False

	return True