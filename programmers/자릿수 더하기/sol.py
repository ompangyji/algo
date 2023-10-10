def solution(n):
    if n<=0 :
        return 0
    else:
        return solution(n/10) + int(n%10)
    

print(solution(1234))