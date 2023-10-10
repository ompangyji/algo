def solution(num_list):
    result = []
    for idx in range(len(num_list)):
        result.append(num_list[len(num_list)-idx-1])

    print(result)

solution([5, 3, 1, 1, 1, 0, 1])