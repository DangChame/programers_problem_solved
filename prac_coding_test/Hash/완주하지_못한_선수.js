function solution(participant, completion) {
    var answer = '';
    
    a = participant.sort();
    b = completion.sort();
    
    final_index = a.length-1;
    answer = a[final_index]
    for (var i = 0; i < b.length; i++)
    {
        if (a[i] != b[i])
            {
                answer = a[i];
                break;
            }
        
    }

    
    return answer;
}
