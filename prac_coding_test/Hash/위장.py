def solution(clo):
	answer = 1
	temp_list = []
	i = 0
	while i < len(clo):
		temp_list.append(clo[i][1])
		i += 1
	count_list = list(set(temp_list))
	i = 0
	while i < len(count_list):
		answer *= temp_list.count(count_list[i]) + 1
		i += 1
	answer -= 1
	return answer



# 테스트 부
nums1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
nums2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	
nums3 = [["aaa", "boo"]]
nums4 = [["crow_mask", "face"], ["yellow_hat", "headgear"]]
nums5 = [["a", "head"], ["b", "head"], ["asdasd", "neck"], ["pwpw", "toe"]]


nums = [nums1,nums2,nums3,nums4, nums5]


result = [5, 3, 1, 3, 11]
i = 0
while (i < len(nums)):
	answer = solution(nums[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1

