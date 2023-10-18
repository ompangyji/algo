import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    #2차원 배열
    matrix = []

    for i in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    board = [[0] * 10 for i in range(10)]

    #board = [[0]*10]*10
    count = 0

    for color in matrix:
        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                if color[-1] == 1:
                    
                    board[i][j] += 1
                    #print(f'i {i} j {j} 빨간색 {board[i][j]}')
                else:
                    
                    board[i][j] += 2
                    #print(f'i {i} j {j} 파란색 {board[i][j]}')

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')

    #N = int(input())

    # arr= [[0]*10 for _ in range(10)]

    # for a in range(N):
    #     r1,c1,r2,c2,color = list(map(int, input().split()))

    #     purple = 0

    #     for i in range(r1, r2 + 1):
    #         for j in range(c1, c2 + 1):
   
    #             arr[i][j] += color 

    #             if arr[i][j] == 3:
    #                 purple += 1
    
    # print(f'#{tc} {purple}')