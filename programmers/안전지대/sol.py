#지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류
#안전한 지역의 칸 수 return
from pprint import pprint
import numpy as np
import pandas as pd

def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# def solution(board):

#     idx = [(ix,iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == 1]

#     for x, y in idx:
#         for i in range(x-1, x+2):
#             for j in range(y-1, y+2):
#                     if i > -1 and j> -1 and len(board) > i and len(board) > j and board[i][j] != 1:
#                             board[i][j] = 1
#                             print(board)
#                             print()        

    
#     answer = 0
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 0:
#                 answer += 1

#     return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
print(solution([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))