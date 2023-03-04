'''
함수
-반복적인 작업을 할때 유용하게 사용가능
-만드는 과정과 사용하는 과정으로 분류할 수 있음
<문법1(연산)>
def 함수이름( ):
    함수내용 작성
함수이름( )
<문법2(입력,연산)>
def 함수이름(입력):
    함수내용작성<입력을 이용할수있음>
{*숫자문자대신 변수로 표기}
{*입력이 여러개라면 쉼표로 구분해서 입력(def 함수이름(입력,입력2,...))}
<문법(입력,연산,출력)>
def 함수이름:
    함수내용 작성
    return 결과
{입력과 결과 모두 변수로 표기}
'''
def 토요일():
    print("와 토요일이다")
토요일()
토요일()

def 일요일(숫자):
    for i in range (숫자):
        print("일요일은 뭐하지?")
일요일(3)
일요일(5)

def 거듭제곱(밑,지수):
    결과=밑**지수
    return 결과
value=거듭제곱(2,8)
print(value)
print(거듭제곱)

def x(num):
    j = []
    for i in range(1, 10):
        j.append(num * i)
    return j

for i in range(2, 10):
    print(i, "단")
    print(x(i))

def multiplication_table(num):
    table = []
    for i in range(1, 10):
        table.append(num * i)
    return table

number = int(input("Enter a number: "))
print("Multiplication table for", number)
print(multiplication_table(number))

