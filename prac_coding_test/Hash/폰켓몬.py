def solution(nums):
	answer = 0

	print(nums)
	nb_of_poket = len(nums) / 2

	nums = set(nums)
	nb_of_set = len(nums)
	if nb_of_set >= nb_of_poket:
		answer = nb_of_poket
	else:
		answer = nb_of_set
	return int(answer)






# 테스트 부
nums1 = [3,1,2,3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]
nums = [nums1,nums2,nums3]


result = [2, 3, 2]
i = 0
while (i < 3):
	answer = solution(nums[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1

