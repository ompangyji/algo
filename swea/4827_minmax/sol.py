import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    numbers = list(map(int,input().split()))

    max = numbers[0]
    min = numbers[0]

    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
        if min > numbers[i]:
            min = numbers[i]
    

    print(f'#{tc} {max-min}')