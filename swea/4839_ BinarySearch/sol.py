import sys
sys.stdin = open('input.txt')

T = int(input())

# 풀이 후
# while문을 함수로 빼보기

#강사님 풀이
for tc in range(1, 1+T):
    # P : 책의 장수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지
    P, A, B = list(map(int, input().split()))

    left = 1
    right = P
    A_count = 0 

    while True:
        center = int((left+right)/2)

        # A의 목적페이지가 가운데보다 왼쪽에 있는경우
        # 오른쪽 데이터를 지우기
        if A < center:
            right = center
        # A의 목적페이지가 가운데보다 오른쪽에 있는경우
        # 왼쪽 데이터를 지우기
        elif center < A:
            left = center
        # A의 목적페이지에 도달한 경우
        else:
            break

        A_count += 1

    left = 1
    right = P
    B_count = 0

    while True:
        center = int((left+right)/2)

        if B < center:
            right = center
        elif center < B:
            left = center
        else:
            break

        B_count += 1

    print(A_count, B_count)

#풀이 전
# def page(l, r, c):
#     su = int((l+r)/2)
#     if c < su:
#         return l, su
#     else:
#         return su, r
#     # else:
#     #     return 0, 0

# for tc in range(1, T+1):
#     P, A, B = list(map(int, input().split())) 
#     #전체 쪽 수, A가 찾을 쪽, B가 찾을 쪽

#     A_search = True
#     B_search = True

#     a = [1, P, A]
#     b = [1, P, B]
  
#     while A_search and B_search:
#         a[0], a[1] = page(a[0], a[1], a[2])
#         b[0], b[1] = page(b[0], b[1], b[2])
        
#         if a[0] == A or a[1] == A:
#             if b[0] == B or b[1] == B:
#                 print(f'#{tc} 0')
#             else:
#                 print(f'#{tc} A')

#             A_search = False
#         elif b[0] == B or b[1] == B:
#             if a[0] == A or a[1] == A:
#                 print(f'#{tc} 0')
#             else:
#                 print(f'#{tc} B')   
#             B_search = False

#         else:
#             continue
    