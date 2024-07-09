# dictionary

dict1 = {1: 'a', 2: 'b', 3: 'c'}
print(dict1)
# 요소 추가
dict1[4] = 'd'
# 요소 삭제
del(dict1[2])
print(dict1)

dict2 = {}
print(dict2)

dict3 = dict()
print(dict3)

# 접근
fruits = {'apple': '사과', 'banana': '바나나', 'peach': '복숭아'}
# print(fruits['tomato'])
print(fruits.get('tomato'))

# 키, 값 변환
print(fruits.keys())
print(list(fruits.keys()))
print(fruits.values())

print("apple" in fruits)

for fruit in fruits.keys():
    print(fruit, ':', fruits[fruit])

# 실습
scores = dict()
scores['Jerry'] = 85
scores['Luna'] = 90
scores['Martin'] = 95
# 추가
scores['Damon'] = 80
# 변경
scores['Jerry'] = 88
# 삭제
del scores['Martin']

# print(score)
for score in scores.keys():
    # print(f"{score}: {scores[score]}")
    print(f"{score}: {scores.get(score)}")

