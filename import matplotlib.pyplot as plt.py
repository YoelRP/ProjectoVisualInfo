import matplotlib.pyplot as plt
plt.axes()
rectangle = plt.Rectangle((0,0), 50, 20, fc='blue',ec="red")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.show()