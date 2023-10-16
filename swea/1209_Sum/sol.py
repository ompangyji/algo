import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())

    matrix = []
    for _ in range(100): #변수 활용하지 않음
        
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    result = []
    for i in range(len(matrix)):
        total_row = 0
        total_top = 0
        total_diag = 0
        total_revdiag = 0
        for j in range(len(matrix)):
            total_row += matrix[i][j]
            total_top += matrix[j][i]
        result.append(total_row)
        result.append(total_top)

        total_diag += matrix[i][i]
        total_revdiag += matrix[i][len(matrix)-1-i]

    result.append(total_diag)
    result.append(total_revdiag)
    
    
    print(f'#{tc} {max(result)}')