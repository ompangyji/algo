import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers1 = list(map(int,input().split()))
    numbers2 = list(map(int,input().split())) # 충전기가 설치된 정류장

    K = numbers1[0] #최대 이동할 수 있는 정류장 수
    N = numbers1[1] #종점
    M = numbers1[2] #충전기가 설치된 수

    count = location = 0

    while location + K < N:
        print(f'버스 위치 {location}')
        for step in range(K, 0, -1):
            print(f'step{step}')
            if (location + step) in numbers2:
                location += step
                count += 1
                break
        else:
            count = 0
            break


            
