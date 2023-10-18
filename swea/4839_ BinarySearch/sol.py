import sys
sys.stdin = open('input.txt')

T = int(input())

def page(l, r, c):
    su = int((l+r)/2)
    if c < su:
        return l, su
    else:
        return su, r
    # else:
    #     return 0, 0

for tc in range(1, T+1):
    P, A, B = list(map(int, input().split())) 
    #전체 쪽 수, A가 찾을 쪽, B가 찾을 쪽

    A_search = True
    B_search = True

    a = [1, P, A]
    b = [1, P, B]
  
    while A_search and B_search:
        a[0], a[1] = page(a[0], a[1], a[2])
        b[0], b[1] = page(b[0], b[1], b[2])
        
        if a[0] == A or a[1] == A:
            if b[0] == B or b[1] == B:
                print(f'#{tc} 0')
            else:
                print(f'#{tc} A')

            A_search = False
        elif b[0] == B or b[1] == B:
            if a[0] == A or a[1] == A:
                print(f'#{tc} 0')
            else:
                print(f'#{tc} B')   
            B_search = False

        else:
            continue
    