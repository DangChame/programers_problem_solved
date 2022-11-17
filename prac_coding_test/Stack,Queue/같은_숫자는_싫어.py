def solution(arr):
	answer = []
	temp = arr[0]
	i = 0
	answer.append(temp)
	while i < len(arr):
		if temp != arr[i]:
			answer.append(arr[i])
			temp = arr[i]
		i += 1
	return answer



# 테스트 부
nums1 = [1,1,3,3,0,1,1]
nums2 = [4,4,4,3,3]


nums = [nums1,nums2]


result = [[1,3,0,1], [4,3]]

i = 0
while (i < len(nums)):
	answer = solution(nums[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1

