def solution(hp):
    #장군개미 = 5, 병정개미 = 3, 일개미 = 1

    return hp//5+hp%5//3+hp%5%3

    # answer = 0
    # answer += (hp//5)
    # temp = hp%5
    # answer += (temp//3)
    # temp = temp%3
    # answer += temp
    # return answer


print(solution(999))