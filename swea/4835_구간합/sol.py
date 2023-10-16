import sys
sys.stdin = open('input.txt')

T = int(input())

#이웃한 M개의 합을 계산
#M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
for tc in range(1, T+1):
    N, M = list(map(int,input().split())) #개수의 정수, 구간의 개수
    numbers = list(map(int,input().split()))

    # sum_list = []
    # for i in range(0, N-M):
    #     sum_list.append(sum(numbers[i:i+M]))
    # print(f'#{tc} {max(sum_list) - min(sum_list)}')

    new=[]
    for i in range(N-M+1):
        result=0
        for j in range(i,i+M):
            result+=numbers[j]
        new.append(result)

    print(f"#{tc} {max(new)-min(new)}")



    # max_sum = 0 
    # min_sum = 0

    # for i in range(N-M+1):
    #     result = 0

    #     for j in range(i, i+M):
    #         result += numbers[j]

    #     if max_sum < result:
    #         max_sum = result
        
    #     print(min_sum, result)
    #     if min_sum > result:
    #         min_sum = result

    
    #     answer = max_sum - min_sum

    # print(f'#{tc} {answer}')