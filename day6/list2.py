'''
index(색인)
-값으로 자리를 찾는 메소드
-중복된 값이 있을 경우 맨 왼쪽만 출력
-리스트에 없는 값은 에러남
indexing<문법>
-자리로 값을 출력하는 문법
-대괄호와 숫자 사용
-left->right 방식은 0부터 시작
-right-left 방식은-1,-2.....으로
insert
-원하는 자리에 값을 추가할때 insert메소드 사용
remove
-원하는 값을 제거 할때 remove메소드 사용
count
-값들의 수를 셀때 count사용
extend,+
-리스트와 리스트 합치기
len
-리스트의 길이를 알고싶을때


'''
a=[100,200,300,400]
print(a.index(300))
print(a.index(100))
a.append(100)
print(a)
print(a.index(100))

b=[100,200,300,400]
print(b[1])
print(b[3])
print(b[0]+b[2])
print(b[-1]-b[1])
print(b[-2]%b[1])

c=["cherry","apple","banana"]
c.insert(1,"orange")
print(c)
c.insert(3,"watermelon")
print(c)
c.remove("cherry")
print(c)

d=[1,2,3,1,4]
print(d.count(1))
print(d.count(2))
print(d.count(5))

e=[1,2,3]
f=[4,5]
e.extend(f)
print(e)
f.extend(e)
print(f)

g=[1,2,3]
h=[4,5]
print(g+h)
print(h+g)

i=[10,20,30]
print(len(i))
i.append(40)
print(len(i))
i.clear()
print(len(i))
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# fruits=["cherry","orange","apple"]
# fruits.append("watermelon")
# fruits.insert(2,"banana")
# fruits.sort()
# fruits.reverse()

# for i in range(len(fruits)):
#     print(fruits[i])

result=[]
for i in range(1,20):
    if i%3==0:
        result.append(i)
print(result)

result=[]
for i in range(len(result)):
    if i%3==0:
        result.append(i)
print(len(result))