import matplotlib.pyplot as plt
plt.figure()
x=[]
x1=[]
x2=[]
x3=[]
y=[]
y1=[]
y2=[]
y3=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(-2*i+1)
# for i in range(-20,21):
#     x.append(i)
#     y.append(-1*i*i+2*i-3)
# for i in range(-10,11):
#     y.append(i)
# #     y.append(2*i*i*i-3)
# for i in range(-10,11):
#     x.append(i)
#     x1.append(i)
#     y.append(2**i)
#     y1.append(1/2**i)
for i in range(-10,11):
    x.append(i)
    x1.append(i)
    x2.append(i)
    x3.append(i)
    y.append(-i)
    y1.append(i*i)
    y2.append(i)
    y3.append(-i*i)
plt.plot(x,y,'o',x1,y1,'o',x2,y2,'o',x3,y3,'o')
plt.show()
# plt.plot(x,y,x1,y1)
# plt.show()
# import numpy as np
# x=[]
# y=[]
# for i in range(-60,70):
#     x.append(i/10)
#     y.append(np.tan(i/10))
# plt.plot(x,y)
# plt.show()


