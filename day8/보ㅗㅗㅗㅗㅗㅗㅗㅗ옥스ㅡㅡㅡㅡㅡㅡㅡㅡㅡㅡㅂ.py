import matplotlib.pyplot as plt
figure,axes=plt.subplots(2,2)
x=[]
x1=[]
x2=[]
y=[]
bar_color=["black"]
bar_color1=["red","blue","green"]
sub=["korea","math","sscience"]
score=[60,90,70]
for i in range(-10,11):

    x.append(i)
    x1.append(i**2)
    x2.append(-i**2)
    y.append(i**3)


axes[0,0].plot(x,x1,'go',x,x2,'ro')
axes[0,1].bar(sub,score,color=bar_color)
axes[1,0].barh(sub,score,color=bar_color1)
axes[1,1].plot(x,y,'black')
plt.show()
