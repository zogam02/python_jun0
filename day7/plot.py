'''
1.모듈설치
2.모듈가져오기
-import 모듈이름
-import as 단축어
3모듈사용하기
-모듈이름.변수
-모듈이름.함수()
'''
# import matplotlib.pyplot
# matplotlib.pyplot.figure()
# matplotlib.pyplot.plot([1,2,3],[4,5,6])
# matplotlib.pyplot.show()


# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot([50,40,60],[150,120,170],'ro')
# plt.ylabel("hight")
# plt.xlabel("weight")
# plt.show()





# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot([0,1,2,3,4,5],[5,8,11,14,17,20],'r')
# plt.ylabel("x")
# plt.xlabel("y")
# plt.show()




# import matplotlib.pyplot as plt

# xvalues=[0,1,2,3,4,5]
# yvalues=[5,8,11,14,17,20]

# plt.figure()
# plt.plot(xvalues,yvalues,'r')
# plt.ylabel("hight")
# plt.xlabel("weight")
# plt.show()





import matplotlib.pyplot as plt

xvalues=[]
yvalues1=[]
yvalues2=[]
yvalues3=[]
for i in range(-10,10):
    xvalues.append(i)
    yvalues1.append(i)
    yvalues2.append(i*i)
    yvalues3.append(i*i*i)


plt.figure()
plt.plot(xvalues,yvalues1,'r',xvalues,yvalues2,'g',xvalues,yvalues3,'b')
plt.ylabel("x")
plt.xlabel("y")
plt.show()





