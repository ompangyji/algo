# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# #풀이 후


#강사님 풀이
# def search(idx):
#     global SUM, MIN_SUM

#     if idx >= N:
#         if SUM < MIN_SUM:
#             MIN_SUM = SUM
#         return

#     # 모든 경우의 수를 탐색
#     for i in range(N):
#         # 해당칸이 비어있다면
#         if check_list[i] == False:
#             # print(idx, i, '=', numbers[idx][i])
#             # result.append(numbers[idx][i])
#             SUM += numbers[idx][i]````
#             check_list[i] = True
#             search(idx+1)
#             # result.pop()
#             SUM -= numbers[idx][i]
#             check_list[i] = False

# for tc in range(1, T+1):
#     N = int(input())

#     numbers = []
#     for _ in range(N):
#         number = list(map(int, input().split()))
#         numbers.append(number)

#     result = []
#     check_list = [False] * N

#     SUM = 0
#     MIN_SUM = 10000000
    
#     search(0)

#     print(MIN_SUM)

#풀이 전, 너무 어렵게 생각해서 구현할 시간이 없었음
# def recursive(n):
#     pass

# for tc in range(1, T+1):
#     N  = int(input())
#     # NxN 배열

#     numbers = []

#     for _ in range(N):
#         number = list(map(int, input().split()))
#         numbers.append(number)

#     min_list = [0] * N
    
#     for _ in range(N):
#         idx, su = recursive()



    

        

        