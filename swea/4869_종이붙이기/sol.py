import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
#강사님 풀이
    N = int(input()) // 10

    memo = [0, 1, 3]

    while N >= len(memo):
        result = memo[len(memo)-2] * 2 + memo[len(memo)-1]
        memo.append(result)

    print(memo[N])

#풀이 전
    # start, end = int(input()) #가로
    # height = 20 #세로
    
    # count = 0

    # def paper(n):
    #     if n == 0:
    #         pass
    #     else:
    #         print(n)
    #         paper(n-10)
    # #print(width)
    # paper(width)

  
    # print(f'#{tc}')