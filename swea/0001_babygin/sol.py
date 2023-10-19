import sys
import numpy as np
sys.stdin = open('input.txt')

#Baby Gin : run과 triplet으로 구성되는 경우
T = int(input())


for tc in range(1, T+1):
    numbers = input()

    counter = [0 for i in range(10)]

    for number in numbers:
        counter[int(number)] += 1

    run = np.where(np.array(counter) == 3)[0]
    triplet = np.where(np.array(counter) == 1)[0]
    if len(run) == 2:
        print(f'{run[0]},{run[0]},{run[0]} {run[1]},{run[1]},{run[1]}')

    if len(run) == 1 and len(triplet) == 3:
        if triplet[0]+1 == triplet[1] and triplet[1]+1 == triplet[2] : 
            print(f'{run[0]},{run[0]},{run[0]} {triplet[0]},{triplet[1]},{triplet[2]}')


            