def solution(lines):
    Max = max(map(max, lines))
    Min = abs(min(map(min, lines)))

    line = [0] * int(Max+Min)

    for x,y in lines:
        line[x+Min:y+Min] = list(map(lambda su: su+1, line[x+Min:y+Min]))


    answer = 0
    for su in line:
        if su > 1:
            answer += 1

    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))