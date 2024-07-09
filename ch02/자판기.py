# 자판기

vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
def check_machine():
    print("남은 음료수: ", vending_machine)
def is_drink():
    if drink in vending_machine:
        return drink
def add_drink():
    vending_machine.append(drink)
def remove_drink():
    vending_machine.remove(drink)

while True:
    who = input("사용자 종류를 입력하세요(1.소비자 2.주인): ")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink():
            print(f'{drink} 드릴께요')
            remove_drink()
        else:
            print(f'{drink}는 지금 없네요')
    else:
        managing = input("할 일 선택(1.추가, 2.삭제): ")
        if managing == '1':
            drink = input("추가할 음료? ")
            add_drink()
            vending_machine.sort()
            print("추가 완료")
            check_machine()
        if managing == '2':
            drink = input("삭제할 음료? ")
            if drink in vending_machine:
                remove_drink()
                print("삭제 완료")
                check_machine()
            else:
                print(f'{drink}는 지금 없네요')
