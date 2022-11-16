def solution_ori(phone_book):
	i = 0
	if len(phone_book) == 1:
		return True
	while i < len(phone_book):
		j = i + 1
		while j < len(phone_book):
			# if len(phone_book[i]) >= len(phone_book[j]):
			# 	index = phone_book[i].find(phone_book[j])
			# else:
			# 	index = phone_book[j].find(phone_book[i])
			# if index == 0:
			# 	return False
			index = phone_book[i].find(phone_book[j])
			index2 = phone_book[j].find(phone_book[i])
			if index == 0 or index2 == 0:
				return False			
			j += 1
		i += 1
	return True

def solution(pp):
	i = 0
	if len(pp) == 1:
		return True
	pp = sorted(pp)
	while i < len(pp) - 1:
		index = pp[i + 1].find(pp[i])
		if index == 0:
			return False
		i += 1
	return True
		

# 테스트 부
nums1 = ["119", "97674223", "1195524421"]	
nums2 = ["1236","123","789"]	
nums3 = ["813", "13"]
nums4 = ["11874", "11"]
nums5 = ["345", "1234567"]
nums6 = ["113"]
nums7 = ["115", "11456", "11578", "112", "12"]

nums = [nums1,nums2,nums3,nums4, nums5, nums6, nums7]


result = [False, False, True, False, True, True, False]
i = 0
while (i < len(nums)):
	answer = solution(nums[i])
	if (answer == result[i]):
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+ "	" + str(i+1)+"번째 correct")
	else:
		print("너의 답 : " + str(answer)+" 정답: " + str(result[i])+"	"+ str(i+1)+"번째 wrong")
	i += 1

