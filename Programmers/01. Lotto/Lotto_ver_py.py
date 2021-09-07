def solution(lottos, win_nums):
    answer = []
    num_of_win =0
    num_of_zero =0
    
    for i in lottos:
        if i == 0:
            num_of_zero+=1
        elif i in win_nums:
            num_of_win+=1
    
    num_of_zero += num_of_win
    if num_of_zero >6:
        num_of_zero = 6
    elif num_of_zero<2:
        num_of_zero =1 
    answer.append(7-num_of_zero)
    if num_of_win<2:
        num_of_win =1 
    answer.append(7-num_of_win)
    return answer