id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi neo"]

k = 1

    
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
    i = 0;
    while (i < len(nb_of_reported)):
        if (nb_of_reported[id_list[i]] >= k):
            nb_of_reported[id_list[i]] = 1
        else:
            nb_of_reported[id_list[i]] = -1
        i += 1
    return nb_of_reported

def make_answer(id_list, dict_suspended, dict_report):
    i = 0
    temp = {}
    temp_list = []
    list_keys = list(dict_report.keys())
    while (i < len(id_list)):
        if id_list[i] in list_keys:
            temp_list.append(id_list[i])
        i += 1
    i = 0
    list_keys = temp_list
    while (i < len(id_list)):
        temp[id_list[i]] = 0
        i += 1
    i = 0
    while (i < len(list_keys)):
        j = 0
        while (j < len(dict_report[list_keys[i]])):
            if (dict_suspended[dict_report[list_keys[i]][j]] == 1):
            	temp[id_list[i]] += 1
            j += 1
        i += 1
    i = 0
    answer = list()
    while (i < len(id_list)):
        answer.append(-1)
        i += 1
    i = 0
    while (i < len(id_list)):
        answer[i] = temp[id_list[i]]
        i += 1
    return answer
                        
def solution(id_list, report, k):
    deoverlaped_report = remove_overlap((report))
    print(report)
    print(deoverlaped_report)
    dict_report = make_dict_report(deoverlaped_report)
    print(dict_report)
    nb_of_reported = count_reported(id_list, deoverlaped_report)
    print(nb_of_reported)
    dict_suspended = check_suspended(id_list, nb_of_reported, k)
    print(dict_suspended)
    answer = make_answer(id_list, dict_suspended, dict_report)
    print(answer)
    
    return answer

print(solution(id_list, report, k))