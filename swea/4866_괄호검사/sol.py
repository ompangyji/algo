import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    code = input()

#강사님 풀이

#풀이 전
    # arrStr = input()


    # brackets = []

    # for chart in arrStr:
    #     if chart =='{' or chart =='}' or chart =='(' or chart ==')':
    #         brackets.append(chart)

    
    # bracket = {'(':0, ')':0, '{':0,'}':0}
    
    # for _ in range(len(brackets)):
    #     temp = brackets.pop(0)
    #     bracket[temp] = bracket[temp]+1

    # if bracket['('] == bracket[')'] and bracket['{'] == bracket['}']:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')