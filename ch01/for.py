
# num = int(input("몇 까지 계산할까요? "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(sum)

# 실습
# second = int(input("몇 초? "))
# for i in range(second, 0, -1):
#     print(i, end=' ')
# print('발사')

# dan = 3
# for i in range(1, 10):
#     # print(f'{dan} x {i} = {dan*i}')
#     # print(dan, "x", i, "=", dan*i)
#     # 형변환
#     print(str(dan) + " x " + str(i) + " = " + str(dan*i))

# for y in range(3):
#     for x in range(2):
#         print(f"y: {y}, x: {x}")
#     print()

n = int(input('몇 줄? '))

for i in range(1, n+1):
    print('*' * i)

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)

# 별이 1, 3, 5로 증가
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))