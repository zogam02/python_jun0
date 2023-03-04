'''
리스트(list)
-열거형 변수를 나타내는 자료구조 중 하나
<문법>
 C=[] #비어있는 리스트
 d=[1,2,3,4] #숫자들을 리스트로 나타냄
<특징1>
추가할때 append 메소드 사용
-맨 오른쪽에만 추가됨
<특징2>
제거할때 pop 메소드 사용
-맨오른쪽 에만 제거됨
<특징3>
전체삭제할 clear 메소드 사용
<특징4>
정렬 (오른차순)할때 sort메소드 사용
<특징5>
역순 정렬할때 reverse 메소드 사용
'''
C=[]
d=[1,2,3,4]
e=["사과","바나나","귤"]
f=[100,"체리",200,"블루 체리"]

print(C)
print(d)
print(e)
print(f)

g=[]
g.append(1)
print(g)
g.append("사과")
g.pop()
g.append(2)
print(g)

h=[1,"사과",2,"블루스컬"]
h.clear()
print(h)

i=[2,4,1,3,]
i.sort()
print(i)

j=["bluebaerry","orange","apple"]
j.sort()
print(j)

k=[2,4,1,3]
k.reverse()
print(k)