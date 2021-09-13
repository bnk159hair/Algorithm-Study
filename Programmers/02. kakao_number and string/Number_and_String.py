def solution(s):
    answer = 0
    solution = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    temp=[]
    temp_answer=[]
    for i in s:
        if i.isalpha():
            temp.append(i)
        elif i.isdigit():
            temp_answer.append(i)
        sum_str = ''.join(temp)
        
        if sum_str in solution:
            temp_answer.append(solution[sum_str])
            temp=[]
    
    temp_answer = list(map(int, temp_answer))
    
    answer=int(''.join(map(str, temp_answer)))
    return answer