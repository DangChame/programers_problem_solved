id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
def solution(id_list, report, k):
	answer = []
	listed_id = list(id_list)
	listed_report = list(report)
	reported_dict = {}
	i = 0
	while i < len(listed_report):
		reported_dict += listed_report[0].split()
		i += 1
		return answer
print(solution(id_list, report, k))