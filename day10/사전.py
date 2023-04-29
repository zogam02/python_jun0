'''
딕셔너리(dictionary)
-python 사용 하는 자료 구조
-key,value의 쌍으로 이루어짐
-중괄호와 :를 이용해 작성
ex){"손흥민":"축구","류현진":"야구"}
-indexing 가능->key를 이용*
              ->get method 이용 ㄱㄴ
-indexing을 이용한 수정 또는 update method쌍을 추가 ㄱㄴ
-"key in dictionary" 질문에 T/F로 확인 ㄱㄴ
'''
# height={"용규":177,"자민":200,"재민":125,"준영":101}
# print(type(height))

# 튜플=(177,200,125,101)



# print(튜플[1])
# print(height["자민"])
# print('jammin say,"what?"')
# 리스트=[177,200,125,101]
# 리스트.pop
# 리스트[1]=150
# print(리스트)
# height["자민"]=150
# height.update({"자민":140})
# height["선생님"]=180
# height.update({"손흥민":185})
# del height["선생님"]
# del height["손흥민"]
# print("용규" in height)
# print("손흥민" in height)
# print(height.keys())
# print(height.values())
# print(height["준영"])
# print(height.get("준영"))
for i in range(10):
    fruits={"o":60,"banana":40,"apple":30}
    fruit=input("This in fruit store. what do you want: ")
    if fruit in fruits:
        print(f"we have {fruit},{fruits[fruit]} left")
    else:
        print(f"sorry, we don't have {fruit}")
    
