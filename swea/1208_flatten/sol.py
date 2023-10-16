import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    num_list = list(map(int,input().split()))
    
    while dump >= 1:      
        if max(num_list) - min(num_list) == 1:
            break
        
        maxIdx = num_list.index(max(num_list))
        minIdx = num_list.index(min(num_list))
        
        num_list[maxIdx] -= 1
        num_list[minIdx] += 1

        dump -= 1

    print(f'#{tc} {max(num_list) - min(num_list)}')
    
