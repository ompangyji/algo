import re

def solution(babbling):
    baby = ["aya", "ye", "woo", "ma" ]

    bab = '/'.join(babbling)
    for char in baby:
        bab=re.sub(char,' ',bab)
    bab = list(bab.split('/'))

    count = 0
    for char in baby:
        if char.find('[a-Z]') == -1:
            print(char)
            count += 1

    return count
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))