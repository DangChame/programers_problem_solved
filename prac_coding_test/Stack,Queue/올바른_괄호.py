
def solution_ori(s):
	temp_list = list(s)
	i = 0
	while i < len(temp_list) - 1:
		if temp_list[i] == '(' and temp_list[i + 1] == ')':
			del temp_list[i]
			del temp_list[i]
			if len(temp_list) == 0:
				return True
			temp_list = "".join(temp_list)
			i = temp_list.find('(')
			if i == -1:
				return False
			temp_list = list(temp_list)

		else:
			i += 1
	if len(temp_list) == 0:
		return True
	return False


def solution_2(s):
	if len(s) % 2 == 1:
		return False
	spare = []
	index_list = []
	i = 0
	while i < len(s):
		index_list.append(i)
		i += 1
	i = 0
	while i < len(s)-1:
		if s[i] == '(' and s[i + 1] == ')':
			spare.append(i)
			spare.append(i + 1)
		i += 1
	while len(spare) != len(s):
		temp = len(spare)
		index_rest = [x for x in index_list if x not in spare]
		i = 0
		while i < len(index_rest)-1:
			if s[index_rest[i]] == '(' and s[index_rest[i + 1]] == ')':
				spare.append(index_rest[i])
				spare.append(index_rest[i] + 1)
			i += 1
		if temp == len(spare):
			return False
	return True

def solution(s):
	if len(s) % 2 == 1 or s[0] != '(' or s[-1] != ')':
		return False
	final_count = [0, 0]
	count_left = 0
	count_right = 0
	i = 0
	while i < len(s):
		if s[i] == '(':
			count_left += 1
		else:
			count_right += 1
		i += 1
	if count_left != count_right:
		return False
	count_left = 0
	count_right = 0
	i = 0
	flag = 'first_attempt'
	while i < len(s):
		while i < len(s) and s[i] == '(':
			i += 1
			count_left += 1
		while i < len(s) and s[i] == ')':
			i += 1
			count_right += 1
		if count_left >= count_right:
			count_left -= count_right
			count_right = 0
			final_count[0] += count_left
			count_left = 0
		else:
			count_right -= count_left
			count_left = 0
			final_count[1] += count_right
			count_right = 0	
		if flag == 'first_attempt' and final_count[1] > final_count[0]:
			return False
		else:
			flag = 'none'
	if final_count[0] != final_count[1]:
		return False
	return True
# 테스트 부
case1 = "())((())"
# "((()((()))))"
#(()())
case2 = "(()())" #3 2 1 2 1 1   1,0 / 0, 1 / 0, 0
#case2 = "( ( ( ) ) ( ) )"  3 2 1 2  1	1  2  [1,0/0,1]
case3 = "((()((()))))"
case4 = "(())())("
case5 = "(()())"
#"( ( ) ) ) ( ( )"  2 3  / 2 1  [0,1 / 1,0]
case6 = "(()())()("
case7 = "("

#짝수여야함,짝의 개수가 맞아야 하고,처음은 (, 마지막은)로 끝나야만 한다

case = [case1,case2,case3,case4,case5,case6,case7]


result = [False, True, True, False,True,False,False]
i = 0
while (i < len(case)):
	answer = solution(case[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1
