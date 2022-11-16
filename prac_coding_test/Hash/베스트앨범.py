def solution(genres, plays):
	answer = []
	count_play = {}
	temp_list = []
	genres_list = list(set(genres))

	i = 0
	while i < len(genres_list):
		count_play[genres_list[i]] = 0
		i += 1
	i = 0
	while i < len(plays):
		count_play[genres[i]] += plays[i]
		i += 1
	count_sorted = sorted(count_play.items(), key=lambda x: x[1], reverse=True)
	i = 0
	while i < len(count_sorted):
		j = 0
		temp_list.clear()
		while j < len(genres):
			if count_sorted[i][0] == genres[j]:
				temp_list.append(plays[j])
			j += 1
		
		temp_list = sorted(temp_list, reverse=True)
		if genres.count(count_sorted[i][0]) != 1:
			if temp_list[0] == temp_list[1]:
				j = 0
				count = 0
				while j < len(plays) and count < 2:
					if temp_list[0] == plays[j]:
						answer.append(j)
						count += 1
					j += 1
			else:
				answer.append(plays.index(temp_list[0]))
				answer.append(plays.index(temp_list[1]))
		else:
			answer.append(plays.index(temp_list[0]))

		i += 1
	return answer


# 테스트 부
nums1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]
nums2 = ["classic", "pop", "classic", "classic" ]
plays2 = [500, 600, 150, 800, ]
nums3 = ["classic","classic", "classic", "classic" ]
plays3 = [500, 600, 600, 600]
nums = [nums1, nums2, nums3]
plays = [plays1, plays2, plays3]

result1 = [4, 1, 3, 0]
result2 = [3,0,1]
result3 = [1, 2]

result = [result1, result2, result3]

i = 0
while (i < len(nums)):
	answer = solution(nums[i], plays[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1