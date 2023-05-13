'''
클래스(class)
-객체(object)를 생성하기 위한 설계도
-생성된 객체는 인스턴스라고 함
-class 내에 맴버 변수는 플로퍼티 라고 함(property)
-class내 에 맴버 함수는 메소드 라고함(method)
-문법:
class class이름:
    프로퍼티
    메소드
*메소드 작성시 입력변수로 self를 반드시 적어줘야함
'''
# def 더하기(a,b):
#     합=a+b
#     return 합
# print(더하기(1,2))
# class 수학:
#     원주율=3.14
#     자연로그e=2.718
#     def 더하기(self,a,b):
#         합=a+b
#         return 합
# 유치원수학=수학()
# print(유치원수학.더하기(1,2))
# 초등수학=수학()
# print(초등수학.원주율)
# 중등수학=수학()
# print(중등수학.원주율)
# 고등수학=수학()
# print(f"{고등수학.원주율},{고등수학.자연로그e}")

class 넓이:
    def 삼각형넓이(self,a,b):
        넓이=a*b/2
        return 넓이
    def 원기둥넓이(self,r,h):
        겉넓이=3.14*r*r*2+2*3.14*r*h
        return 겉넓이
    def 원기둥부피(self,r,h):
        부피=3.14*r*r*h
        return 부피
초등수학=넓이()
중등수학=넓이()
base=input("밑변을 입력하시오: ")
height=input("높이를 입력하시오: ")
height1=input("높이를 입력하시오: ")
vangeleram=input("반지름을 입력하시오: ")
print(f"반지름{vangeleram}이고,높이가{height1}면,원기둥 겉넓인는{중등수학.원기둥넓이(int(vangeleram),int(height1))}이고 원기둥 부피는{중등수학.원기둥부피(int(vangeleram),int(height1))}입니다")
print(f"밑변이{base}이고,높이가{height}일때,삼각형 넓이는{초등수학.삼각형넓이(int(base),int(height))}입니다")
