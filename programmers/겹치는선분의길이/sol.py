def solution(lines):
    print()
    Max = max(map(max, lines))
    Min = abs(min(map(min, lines)))

    print(Max+abs(Min))
    line = [0] * int(Max+Min)

    for x,y in lines:
        print(x,y)



    

    # return answer


print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))