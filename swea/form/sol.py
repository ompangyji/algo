import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    number = input()
    print(number)

    #2차원 배열
    matrix = []

    for _ in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    print(f'#{tc}')