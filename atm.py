# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료 => 글자를 입력받을지 / 숫자를 입력받을지
# 숫자로 원하는 기능을 입력할 수 있게 만들어주섿요. 그리고 사용자가 입력한 기능을 num에 넣어주세요.
# deposit_amount: 

balance = 3000

while True:
    num = input("사용하실 기능의 번호를 선택하세요. 1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료)")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요 : ") # *** isdigit => 숫자 = True, 문자 = False
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount) # balance = balance + int(deposit_amount) => 재할당
            print(f"입금하신 금액 {deposit_amount}원이 입금 완료되었습니다. 현재 잔액은 {balance}입니다.")
        else:
            print("정신차리고, 제대로 된 숫자형태로 입력해 이자식아")

    if num == "2":
        pass

    if num == "3":
        pass

    if num == "4":
        print("서비스를 종료합니다.")
        break