import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    start, end = int(input()) #가로
    height = 20 #세로
    
    count = 0

    def paper(n):
        if n == 0:
            pass
        else:
            print(n)
            paper(n-10)
    #print(width)
    paper(width)

  
    print(f'#{tc}')