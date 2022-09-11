
s = "3people unFollowed me"

s = "333A a AaA aa2a    a111   AA 2A2A"


def solution(s):
	answer = ''
	splited = s.split()
	i = 0
	listofanswer = []
	while (i < len(splited)):

		splited[i] = splited[i].lower()
		temptemp = list(splited[i])
		if (temptemp[0] <= 'z' and 'a' <= temptemp[0]):
			temptemp[0] = temptemp[0].upper()
		tempjoined = ''.join(temptemp)
		listofanswer.append(tempjoined)
		i += 1
	tempanswer = ' '.join(listofanswer)
	answer = tempanswer
	return answer


def solution(s):
	templist = list(s)
	first_encounter = 1
	i = 0
	while (i < len(s)):
		if templist[i] == ' ':
			first_encounter = 1
			i += 1
		elif first_encounter == 1 and ('A' <= templist[i] and templist[i] <= 'Z'):
			first_encounter = -1
			i += 1
		elif first_encounter == 1 and ('0' <= templist[i] and templist[i] <= '9'):
			first_encounter = -1
			i += 1
		else:
			if first_encounter == 1 and ('a' <= templist[i] and templist[i] <= 'z'):
				templist[i] = templist[i].upper()
				first_encounter = -1

			elif first_encounter == -1 and ('A' <= templist[i] and templist[i] <= 'Z'):
				templist[i] = templist[i].lower()
				first_encounter = -1


			elif i == 0 and ('0' <= templist[i] and templist[i] <= '9'):
				first_encounter = -1
			i += 1
	answer = ''.join(templist)
	return answer
print(solution(s))
