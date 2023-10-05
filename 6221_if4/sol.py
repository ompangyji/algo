#-*- coding:utf-8 -*-

import sys
sys.stdin = open('input.txt', encoding='UTF8')

Man1 = input()
Man2 = input()


# if Man1 == Man2:
#     print('Result : Draw')
# elif Man1 == '바위':
#     if Man2 == '가위':
#         print('Result : Man1 Win!')
#     else:
#         print('Result : Man2 Win!')

# elif Man1 == '가위':
#     if Man2 == '보':
#         print('Result : Man1 Win!')
#     else:
#         print('Result : Man2 Win!')
# else:
#     if Man2 == '바위':
#         print('Result : Man1 Win!')
#     else:
#         print('Result : Man2 Win!')

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(Man1)
man2_idx = rcp.index(Man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    print(f'Result : Man{-3+result} Win!')