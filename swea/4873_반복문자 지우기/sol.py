import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pass
#강사님 풀이
    string = input()

    stack = []

    for char in string:
        # 스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(char)
        # 스택이 비어있지 않은경우 => 비교를 할 수 있는 상태
        else:
            # 제일 마지막 데이터와 비교하는 데이터가 일치하는경우
            if char == stack[-1]:
                stack.pop()
            # 일치하지 않은경우
            else:
                stack.append(char)

    print(stack)

#풀이 전
    # arrStr = list(input())

    
    # run = True
    # now = 0
    # #ABCCB
    # while run:
    #     print(f'{now} {arrStr[now]} vs {now+1} {arrStr[now+1]}++')
    #     if arrStr[now] == arrStr[now+1]:
    #         arrStr.pop(now)
    #         arrStr.pop(now)
    #         print('pop()')
    #         print(arrStr)

    #         for i in range(len(arrStr)-1):
    #             print(f'{i} {arrStr[i]} vs {i+1} {arrStr[i+1]}')
    #             if arrStr[i] == arrStr[i+1]:
    #                 now = -1
    #                 run = True
    #             else:
    #                 run = False
                    
    #     now += 1

    #print(f'#{tc} {len(arrStr)}')
            

    #print(arrStr)