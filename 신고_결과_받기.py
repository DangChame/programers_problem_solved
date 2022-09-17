id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi neo"]
id_list = ["1", "2", "3", "4", "5", "6", "7"]
report = ["1 3", "1 2", "6 2", "4 3", "7 1", "1 3", "3 1","4 2"]
k = 2

    
def make_dict_report(listed_report):
    i = 0
    temp = {}
    while (i < len(listed_report)):
        temp[listed_report[i].split()[0]] = ""
        i += 1
    i = 0
    while (i < len(listed_report)):
        if len(temp[listed_report[i].split()[0]]) == 0:
            temp[listed_report[i].split()[0]] = list()
            temp[listed_report[i].split()[0]].append(listed_report[i].split()[1])
            
        else:
            temp[listed_report[i].split()[0]].append(listed_report[i].split()[1])
        i += 1
    
    return temp

def count_reported(id_list, report_deoverlaped):
    i = 0
    temp = {}
    while (i < len(id_list)):
        temp[id_list[i]] = 0
        i += 1
    i = 0
    while (i < len(report_deoverlaped)):
        temp[report_deoverlaped[i].split()[1]] += 1
        i += 1
    return temp
    
def remove_overlap(report):
    temp = list(set(report))
    return temp
    
def check_suspended(id_list, nb_of_reported, k):
    i = 0
    while (i < len(nb_of_reported)):
        if (nb_of_reported[id_list[i]] >= k):
            nb_of_reported[id_list[i]] = 1
        else:
            nb_of_reported[id_list[i]] = -1
        i += 1
    return nb_of_reported

def make_answer(id_list, dict_suspended, dict_report):
    answer = [0 for i in range(len(id_list))]

    list_keys = list(dict_report.keys())

    i = 0
    while (i < len(list_keys)):
        j = 0
        while j < len(dict_report[list_keys[i]]):
            if dict_suspended[dict_report[list_keys[i]][j]] == 1:
                answer[id_list.index(list_keys[i])] += 1
            j += 1
        i += 1
    return answer
    
def solution(id_list, report, k):
    deoverlaped_report = remove_overlap((report))

    dict_report = make_dict_report(deoverlaped_report)

    nb_of_reported = count_reported(id_list, deoverlaped_report)

    dict_suspended = check_suspended(id_list, nb_of_reported, k)

    answer = make_answer(id_list, dict_suspended, dict_report)

    
    return answer

print(solution(id_list, report, k))