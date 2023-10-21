# N 마리 중 N/2마리를 가져가도 좋다함.
# 같은 종류의 폰켓몬은 같은 번호를 가진다. 중복 제거
# 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

def recursion(n):
    if n <= 1:
        return 1
    else:
        return recursion(n-1)*n

def solution(nums):
    mon = set(nums)

    print(len(mon))
    answer = recursion(len(mon))
    return answer


solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])