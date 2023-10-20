import sys
sys.stdin = open('input.txt')

#주어진 조건에 따라 피자를 구울 때, 
#화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.
T = int(input())

for tc in range(1, T+1):

#풀이 후
    N, M = list(map(int, input().split()))
    # N : 화덕 크기, M : 피자 개수

    pizza = list(map(int, input().split()))
    que = [i for i in range(0,N)]
    remain = []

    while True:
        if len(que) > 1:
            
            #피자 꺼내기
            output = que.pop(0)
   
            #꺼내서 치즈가 반으로 줄어든다.
            pizza[output] //= 2

            if pizza[output] != 0 :
                #피자 다시 넣기
                que.append(output)
        else:
            break

    print(f'#{tc} {que[0]+1}')
    

# 강사님 풀이


#풀이 전 / 화덕에 들어가는 N개를 고려하지 않음..
    # N, M = list(map(int, input().split()))
    # # N : 화덕 크기, M : 피자 개수

    # pizza = list(map(int, input().split()))
    # que = [i for i in range(0,M)]

    # while True:
    #     if len(que) > 1:
            
    #         #피자 꺼내기
    #         output = que.pop(0)
   
    #         #꺼내서 치즈가 반으로 줄어든다.
    #         pizza[output] //= 2

    #         if pizza[output] != 0 :
    #             #피자 다시 넣기
    #             que.append(output)
    #     else:
    #         break

    # print(f'#{tc} {que[0]+1}')
    


    