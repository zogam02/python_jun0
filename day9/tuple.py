'''
튜플(tuple)
-python의 자료구조중 하나
-여러 값들을 모아둔 형태로 list 유사
-list와 같이 indexing,slicing ㄱㄴ
-list와 달리 소괄호 이용


-튜플과 리스트의 차이점
  -리스트의 값은 mutableㅎㅏㅁ
  -튜플 값은 immutableㅎㅏㅁ
'''
# a=[1,2,3]
# a[2]=100
# print(a)
# b=(1,2,3)

# print(type(a),type(b))
# print(a[2],b[2])
a=[1,2,3]
a[1]=10
a[2]=100
print(a)
b=(1,2,3)
b[2]=100
print(b)