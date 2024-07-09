
number = int(input("자연수: "))

if number % 2 == 0:
    print("짝수")
if number % 2 != 0:
    print("홀수")

age = int(input('나이: '))
gender = input("여 or 남")
if age < 20:
    print("미성년자입니다.")
elif age < 30:
    if gender == '여':
        print("20대 입니다.")
elif age < 40:
    print("30대 입니다.")
else:
    print("이제는 중년.")