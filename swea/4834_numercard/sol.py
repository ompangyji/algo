import sys
sys.stdin = open('input.txt')

import numpy as np
T = int(input())

for tc in range(1, T+1):
    N = int(input()) #카드 수
    numbers = input()  #카드

    counter = [0 for i in range(10)]

    for number in numbers:
        counter[int(number)] += 1

    max = 0
    max_card = 0

    for i in range(10):
        if max <= counter[i]:
            max = counter[i]
            max_card = i

    print(f'#{tc} {max_card} {max}')
  

  