def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])
    return answer



print(solution([1,2,3,4,5], 1, 3))