import re

def solution(my_string):
    answer = re.findall('\d',my_string)
    answer = sum(list(map(int, answer)))
    return answer

solution('aAb1B2cC34oOp')
solution('1a2b3c4d123')