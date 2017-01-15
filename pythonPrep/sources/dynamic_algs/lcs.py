
import io

def longest_common_subsequence(a, b):
	""" 
	Return the longest common subsequence of two string inputs. 

	Adapted from
	Source:http://rosettacode.org/wiki/Longest_common_subsequence#Python
	"""

	lengths = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

	for index_a, char_a in enumerate(a):
		for index_b, char_b in enumerate(b):
			
			if char_a == char_b:
				lengths[index_a+1][index_b+1] = lengths[index_a][index_b] + 1
			
			else:
				prev_row = lengths[index_a][index_b+1]
				prev_col = lengths[index_a+1][index_b]

				lengths[index_a+1][index_b+1] = max(prev_row, prev_col)

	output = io.StringIO()

	a_i, b_i = len(a), len(b)

	# Backtrack
	while a_i > 0 and b_i > 0:
		if lengths[a_i][b_i] == lengths[a_i-1][b_i]:
			a_i -= 1
		elif lengths[a_i][b_i] == lengths[a_i][b_i-1]:
			b_i -= 1
		else:
			assert a[a_i-1] == b[b_i-1]
			output.write(a[a_i-1])
			a_i -= 1
			b_i -= 1

	result = output.getvalue()[::-1]
	output.close()

	return result

def longest_common_substring(str1, str2):
	""" 
	Return the longest common substring of two string inputs. 

	Time: O( |str1| * |str2| ) 
	Space: O( |str1| * |str2| ) 
	"""

	matrix = [[ 0 for _ in range(len(str2)+1) ] for _ in range(len(str1)+1)]

	result_length = 0
	
	output = io.StringIO()

	for index_1 in range(1, len(matrix)):
		for index_2 in range(1, len(matrix[index_1])):
			char_1 = str1[index_1 - 1]
			char_2 = str2[index_2 - 1]

			if char_1 == char_2:
				current_substring_length = matrix[index_1 - 1][index_2 - 1] + 1
				matrix[index_1][index_2] = current_substring_length
				
				if result_length < current_substring_length:
					result_length = current_substring_length

					# Amortized O(1) ?
					output.close()
					output = io.StringIO()
					output.write(str1[index_1 - result_length: index_1])

				elif result_length == current_substring_length:
					output.write(char_1)

	result_substring = output.getvalue()
	output.close()

	return result_substring