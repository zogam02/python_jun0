'''
조건문
1.if,else                       (들여쓰기:space,tab)
if 조건:
    참일때 작성
else:
    거짓일때 작성
2.for
for 변수 in range(숫자):
    작성

for 변수 in range(시작 숫자,끝 숫자):
    작성

for 변수 in range(시작 숫자,끝 숫자,증감):
    작성
 
'''
# apple=10
# orange=20
# if apple<orange:
#     print("사과가 큼")
# else:
#     print("오렌지가 큼")

# for i in range(3):
#     print("안녕")

# for i in range(1,11):
#     print(i)

# for i in range(2,11,2):
#     print(i)

# for i in range(1,11):
#     if i%2==1:
#         print(i)

# for i in range(1,11):
#     if i%2==0:
#         print(i)
sum=0
for i in range(20,41):
    if i%3!=0:
        sum+=i
print(sum)

for i in range(50,101):
    if i%3==0:
        if i%4==0:
            print(i)
sum=0
sum1=0
for i in range(1,101):
    if i%2==0:
       sum+=i

    if i%2==1:
        sum1+=i
print(sum-sum1)

mul=1
for i in range(10,31):
    if i%9==0:
        mul*=i
print(mul)
