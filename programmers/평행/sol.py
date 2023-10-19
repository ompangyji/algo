#주어진 네 개의 점을 두 개씩 이었을 때, 
#두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return
import numpy as np

def gradient(dot1,dot2):
    return abs((dot2[1]-dot1[1])/(dot2[0]-dot1[0]))


def solution(dots):
    #[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots 이런 할당 방법도 있음

    gradient1 = [gradient(dots[0], dots[1]), gradient(dots[2], dots[3])]
    gradient2 = [gradient(dots[0], dots[2]), gradient(dots[1], dots[3])]

    if gradient1[0] == gradient1[1] or gradient2[0] == gradient2[1]:
        return 1
    else:
        return 0
    
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
print(solution([[1, 2], [5, 1], [3, 6], [6, 3]])) #1
print(solution([[0, 0], [6, 6], [2, 3], [3, 2]]))