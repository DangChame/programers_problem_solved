

s = "110010101001"


def reduce(s):
	count_zero = 0;
	i = 0;
	temp_list = list(s)
	while (i < len(temp_list)):
		if (temp_list[i] == '0'):
			count_zero += 1
			del(temp_list[i])
		else:
			i += 1
	answer = ''.join(temp_list)
	return count_zero, answer

def solution(s):
	deleted_zero = 0
	nb_of_excuted = 0
	temp_answer = s
	while (temp_answer != '1'):
		temp_zero, temp_answer = reduce(temp_answer)
		deleted_zero += temp_zero
		nb_of_excuted += 1
		len_of_str = len(temp_answer)
		to_binary = bin(len_of_str)
		to_binary = to_binary[2:]
		temp_answer = to_binary



	return nb_of_excuted, deleted_zero


print(solution(s))
