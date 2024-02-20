# Basc Matplotlib example
import numpy as np
import matplotlib.pyplot as plt

xlist = []
ylist = []
for x in range(8):
    xlist.append(x)
    ylist.append(x * 3)

x = np.array(xlist)
y = np.array(ylist)

plt.title("My First Mat Plot")
plt.xlabel("Average count")
plt.ylabel("Sales (Rs.)")

plt.plot(x, y)

plt.grid()
plt.show()
