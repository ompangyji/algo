import re

def solution(babbling):
    # baby = ["aya", "ye", "woo", "ma" ]

    # bab = '/'.join(babbling)
    # for char in baby:
    #     bab=re.sub(char,' ',bab)
    # bab = list(bab.split('/'))

    # count = 0
    # for char in bab:
    #     if re.match('\s+$',char):
     
    #         count += 1

    # return count

    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))