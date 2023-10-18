import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    #글자판 크기, 화문 문자 길이
    arrStr = []

    for _ in range(N):
        arrStr.append(input())

    #세로 데이터 저장
    colStr = []
    for i in range(0, N):
        col = ''
        for j in range(0, N):
            col += arrStr[j][i]
        colStr.append(''.join(col))

    for row, col in zip(arrStr, colStr):
        for i in range(0,N-M+1):
            end = M+j
            #가로 비교
            if row[i:end] == row[i:end][::-1]:
                result = row[i:end]
            #세로 비교
            if col[i:end] == col[i:end][::-1]:
                result = col[i:end]

    print(f'#{tc} {result}')      
        
                     

    