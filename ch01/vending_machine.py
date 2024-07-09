'''
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

print("============== RESTART")
drink = input("마시고 싶은 음료? ")
if drink in vending_machine:
    print(f'{drink} 드릴께요')
else:
    print(f'{drink}는 지금 없네요')
'''

#조건1. 사용자는 소비자, 주인 두 가지 종류로 입력받기(번호 또는 값 입력)
#조건2. 소비자일때 마시고 싶은 음료 입력받기
#조건2-1. 값이 있으면 vending_machine에서 제거, 없으면 없음 출력
#조건3. 주인일때 추가, 삭제 두 가지 종류 입력 받기
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

while True:
    who = input("사용자 종류를 입력하세요(1.소비자 2.주인): ")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if drink in vending_machine:
            print(f'{drink} 드릴께요')
            vending_machine.remove(drink)
        else:
            print(f'{drink}는 지금 없네요')
    else:
        managing = input("할 일 선택(1.추가, 2.삭제): ")
        if managing == '1':
            drink = input("추가할 음료? ")
            vending_machine.append(drink)
            vending_machine.sort()
            print("추가 완료")
            print("남은 음료수: ", vending_machine)
        if managing == '2':
            drink = input("삭제할 음료? ")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print("삭제 완료")
                print("남은 음료수: ", vending_machine)
            else:
                print(f'{drink}는 지금 없네요')
