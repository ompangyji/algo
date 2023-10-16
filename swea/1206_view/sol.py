import sys
sys.stdin = open('input.txt')

T = 1

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int,input().split()))

    for now in range(N):
        if now == 0:
            continue
        else:
            idx = [-2, -1, 1, 2]


    print(f'#{tc} {left+right}')