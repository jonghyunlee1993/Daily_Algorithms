# greedy 알고리즘으로 해결
def solution(number, k):
    collected = []
    
    for i, num in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += number[i:]
            break
        
        collected.append(num)
    
    answer = "".join(collected)
    return answer[:-k] if k > 0 else answer
    

# 시간 초과 문제 있음

from itertools import permutations, combinations
from functools import reduce

def solution(number, k):
    split_number = []
    
    # poss_numbers = list(permutations(list(number), len(number) - k))
    poss_numbers = list(combinations(list(number), len(number) - k))
    
    for poss_number in poss_numbers:
        split_number.append(int(reduce(lambda sub, ele: sub + ele, poss_number)))

    return str(max(split_number))