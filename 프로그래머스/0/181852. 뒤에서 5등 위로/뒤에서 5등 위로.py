def solution(num_list):
    answer = sorted(num_list)
    del answer[:5]
    return answer