import sys
sys.stdin = open('input.txt')

TC = input()   #<-int(input()) 단일 정수

for i in range(int(TC)):
    num = int(input())

    if num % 2 ==1 :
        print('홀수')
    else:
        print('짝수')


# numbers = input().split()

# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 ==1:
#         print(f,'{int_num}은 홀 수 있습니다.')

numbers = list(map(int, input().split()))
print(numbers)

for number in numbers : 
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')