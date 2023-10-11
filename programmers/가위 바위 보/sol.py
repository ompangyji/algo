def solution(rsp):
    #가위 = 2, 바위 = 0, 보 = 5
    # answer = ''
    # for chart in rsp:
    #     if chart == '2':
    #         answer += '0'
    #     elif chart == '0':
    #         answer += '5'
    #     else:
    #         answer += '2'
    # return answer

    answer = {'0':'5','2':'0','5':'2'}
    return ''.join(answer[i] for i in rsp)

print(solution('205'))