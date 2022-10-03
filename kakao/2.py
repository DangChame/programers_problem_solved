

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]



def one_cycle(capacity, do_list, position):
	count = 0
	to_return_position = position
	while capacity != 0 and position >= 0:
		if do_list[position] == 0:
			position -= 1
		else:
			if count == 0:
				to_return_position = position
			count += 1
			capacity -= 1
			do_list[position] -= 1
	return do_list, to_return_position
			
			

def solution(cap, n, deliveries, pickups):
	sum_of_todeliv = sum(deliveries)
	sum_of_pickups = sum(pickups)
	answer = 0
	while sum_of_pickups > 0 and sum_of_todeliv > 0:
		position = n - 1
		deliveries, temp1 = one_cycle(cap, deliveries, position)
		pickups, temp2 = one_cycle(cap, pickups, position)
		if temp1 > temp2:
			answer += (temp1 + 1) * 2
		else:
			answer += (temp2 + 1) * 2
		sum_of_todeliv -= cap
		sum_of_pickups -= cap


	return answer


print(solution(cap, n, deliveries, pickups))