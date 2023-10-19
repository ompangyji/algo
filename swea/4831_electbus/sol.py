import sys
sys.stdin = open('input.txt')

T = int(input())

#강사님 풀이
for tc in range(1, T+1):
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수

    K, N, M = list(map(int, input().split()))

    bus_stop = list(map(int, input().split()))

    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우  ←←←←
    if K >= N:
        count = 0
    # 충전을 하면서 지나가야 하는 경우
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재위치(now)를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            #-↓↓↓↓↓-
            for i in range(now+K, now, -1):  # 뒤에부터 탐색해서 앞으로 이동
                # 1. 최대범위가 종점을 넘는경우
                if i >= N:
                    now = N
                    break

                # 2. 최대범위가 종점을 넘지 않은경우
                if i in bus_stop:
                    now = i  # 충전기가 있다면 현재 위치로 now를 변경
                    count += 1
                    break

            # 현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면 => 도착 불가능
            else:
                count = 0
                now = N

    print(f'#{tc} {count}')

#풀이 전
# for tc in range(1, T+1):
#     numbers1 = list(map(int,input().split()))
#     numbers2 = list(map(int,input().split())) # 충전기가 설치된 정류장

#     K = numbers1[0] #최대 이동할 수 있는 정류장 수
#     N = numbers1[1] #종점
#     M = numbers1[2] #충전기가 설치된 수

#     count = location = 0

#     while location + K < N:
#         print(f'버스 위치 {location}')
#         for step in range(K, 0, -1):
#             print(f'step{step}')
#             if (location + step) in numbers2:
#                 location += step
#                 count += 1
#                 break
#         else:
#             count = 0
#             break


            
