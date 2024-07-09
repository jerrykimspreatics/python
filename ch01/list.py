a = [1, 2, 3]
b = [4, 5]

print(a + b)
print(a * 2)
print(len(b))

# alphabet = ['b', 'd', 'a', 'c']
#
# alphabet.sort()
# print(alphabet)
#
# alphabet.reverse()
# print(alphabet)

# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# print(rainbow.index('yellow'))
#
# rainbow.append("white")
# print(rainbow)
#
# del rainbow[2:6]
# print(rainbow)

# 실습
n = int(input("입력: "))
arr = []
for i in range(1, n+1):
    arr.append(i)
print(arr)

# 반복문 사용
result1 = []
for i in ['a', 'b', 'c']:
    result1.append(i.upper())
print(result1)

# map(함수, 반복가능한 객체)
def cap(str):
    return str.upper()

result2 = map(cap, ['a', 'b', 'c'])
print(list(result2))

# 실습
'''
input_nums = input("숫자 여러 개 입력> ").split()
# numbers = [20, 40, 10, 50]
numbers = []
for i in input_nums:
    numbers.append(int(i))
print(numbers)

# 최대값
max_val = numbers[0]
for i in numbers:
    if i > max_val:
        max_val = i
print(max_val)

max_val = max(numbers)
min_val = min(numbers)
print("최대값: ", max_val)
print("최소값: ", min_val)

# 나머지 값 평균 계산
numbers.remove(max_val)
numbers.remove(min_val)
print(numbers)

average = sum(numbers) / len(numbers)
print("나머지 값의 평균: ", average)
'''