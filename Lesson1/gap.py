def dec_to_bin(N):
	return "{0:b}".format(N)

def number_max_of_gaps(binary_number):
	max = 0
	counter = 0
	for c in binary_number:
		if c == '0':
			counter = counter + 1
		else:
			if counter > max:
				max = counter
			counter = 0
	return max

def binary_gap(N):
	binary_string = dec_to_bin(N)
	return number_max_of_gaps(binary_string)

def solution(N):
	return binary_gap(N)


