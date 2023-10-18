import sys
sys.stdin = open('input.txt')

T = int(input())

def page(l, r):
    return int((l+r)/2)

for tc in range(1, T+1):
    su = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()

    result=''
    for i in range(5):
        result += str(numbers[-1*(i+1)]) + ' '
        result += str(numbers[i]) + ' '

    print(f'#{tc} {result}')