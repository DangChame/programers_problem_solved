#https://school.programmers.co.kr/learn/courses/30/lessons/12939
s = "-1 -2 -3 -4"
def solution(s):
	answer = ''
	splited = s.split()
	splited[0] = int(splited[0])
	splited[1] = int(splited[1])

	if splited[0] <= splited[1]:
		min = splited[0]
		max = splited[1]
	else:
		min = splited[1]
		max = splited[0]
	
	i = 2;
	min = int(min)
	max = int(max)
	if len(splited) > 2:
		while i < len(splited):
			splited[i] = int(splited[i])
			if splited[i] <= min:
				min = splited[i]

			if splited[i] >= max:
				max = splited[i]

			i += 1
	answer = str(min) + " " + str(max)
	return answer

print(solution(s))