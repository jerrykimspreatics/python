
"""
교통비
나이  8세 미만
카드
현금

"""

age = int(input("나이를 숫자로 입력해주세요: "))
payment = input("결재 방법을 입력해주세요('카드' 또는 '현금'만 입력): ")

if age < 8:
    charge = "무료"
elif age < 14:
    charge = "450원"
elif age < 20:
    if payment == "카드":
        charge = "720원"
    else:
        charge = "1000원"
elif age < 75:
    if payment == "카드":
        charge = "1200원"
    else:
        charge = "1300원"
else:
    charge = "무료"
print(str(age) + "세의 요금은 " + charge + "입니다.")
print(f'{age}세의 {payment} 요금은 {charge}입니다.')
