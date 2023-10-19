import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    #V : 노드 수, E : 간선 수
    V, E = list(map(int, input().split()))
    
    nodes = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node[0]
        end = node[1]

        nodes[start][end] = 1
    
    pprint(nodes)

    S, G = list(map(int, input().split()))

    



    print(f'#{tc}')