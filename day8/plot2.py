import matplotlib.pyplot as plt
# fruits=["apple","banana","cherry","orange"]
# counts=[4,7,6,9]
# figure,axes=plt.subplots(2,1)
# axes[1].plot (fruits,counts)
# axes[0].plot (fruits,counts)
# plt.show()
# plt.figure()
# plt.plot([0,5],[5,0],[0,5],[-5,0])
figure,axes=plt.subplots(1,2)
axes[0].plot([0,5],[5,0])
axes[1].plot([0,5],[-5,0])
plt.show()



