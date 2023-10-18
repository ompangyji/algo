import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    #N 파리 구간, M 내려치는 구간

    #2차원 배열
    matrix = []

    for _ in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    result = []
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    total += matrix[k][l]
                  
                result.append(total)

    print(f'#{tc} {max(result)}')                                      