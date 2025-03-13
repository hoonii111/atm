# 💰 ATM Program

## 📜 개요
이 프로그램은 간단한 은행 서비스 기능을 제공합니다. 사용자는 입금, 출금, 영수증 보기, 종료 기능을 선택하여 가상의 은행 잔액을 관리할 수 있습니다.

---

## 📂 주요 기능
1. **입금 기능**:
   - 사용자가 입력한 금액을 잔액에 추가합니다.
   - 입금 내역이 영수증에 기록됩니다.

2. **출금 기능**:
   - 사용자가 입력한 금액을 잔액에서 차감합니다.
   - 출금 금액이 잔액을 초과할 경우, 잔액만큼만 출금됩니다.
   - 출금 내역이 영수증에 기록됩니다.

3. **영수증 보기**:
   - 입출금 내역과 잔액 변동 기록을 확인할 수 있습니다.
   - 기록이 없을 경우, "영수증 내역이 없습니다." 메시지가 출력됩니다.

4. **종료 기능**:
   - 프로그램을 종료하며, 마지막 잔액을 표시합니다.

---

## 🛠️ 사용 방법

1. Python 3.x가 설치되어 있는지 확인합니다.
2. 프로그램 파일(`bank_service.py`)을 실행합니다.
3. 프로그램 실행 후 아래 메뉴 중 하나를 선택합니다:
    1:입금,2:출급,3:영수증 보기,4:종료
4. 각 기능에 따라 입력을 진행합니다:
- **입금**: 금액 입력 후 잔액이 업데이트됩니다.
- **출금**: 금액 입력 후 잔액이 차감됩니다.
- **영수증 보기**: 입출금 기록을 확인합니다.
- **종료**: 프로그램을 종료합니다.

5. 프로그램 종료 시, 마지막 잔액과 함께 종료 메시지가 출력됩니다.

---

## 🧩 사용 화면

### 프로그램 실행


---

## 🐛 에러 처리
- 입력 값이 숫자가 아니거나 음수일 경우, 경고 메시지가 출력됩니다.
- 잘못된 메뉴를 선택하면 "유효하지 않은 선택입니다." 메시지가 출력됩니다.

---

## 📋 요구사항
- Python 3 이상
- 기본적인 터미널 환경

---

## 📧 문의
개발과 관련된 질문이 있다면 언제든지 아래 이메일로 문의해주세요:
- **Email**: eoeo4652@naver.com
​
