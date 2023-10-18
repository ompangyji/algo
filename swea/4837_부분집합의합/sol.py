import sys
sys.stdin = open('input.txt')

T = int(input())
##파이썬 튜터 확인해보기
for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int,input().split())) #부분집합 원소의 수, 부분집합의 합
    
    count = 0

    for i in range(1<<len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1<<j):
                temp.append(numbers[j])
        if sum(temp) == K and len(temp) == N:
            count += 1
            

    print(f'#{tc} {count}')