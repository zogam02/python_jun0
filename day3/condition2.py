'''
조건문(while)
반복할 때 사용
<문법>
while 조건:
    실행할 코드
1.조건이 참이면 실행
2.조건이 거짓이면 while 종료
a=0
while a<0:
    print("안녕")
안녕이 무한
'''
# a=0
# while a<3:
#     print("안녕")
#     a+=1        # a+=1 = a=a+1

# 1.
# a=1
# while a<11:
#     print(a)
#     a+=1
# 2.
# i=1
# while i<11:
#     if i%2==0:
#         print(i)
#     i+=1
# 3.
# i=1
# sum=0
# while i<21:
#     if i%4!=0:
#         sum+=i
#     i+=1
# print(sum)
# 4.
# i=50
# while i<101:
#     if i%3==0:
#         if i%2==0:
#             print(i)
#     i+=1
# 5.
a=1
mul=1
sum=0
while a<11:
    if a%4==0