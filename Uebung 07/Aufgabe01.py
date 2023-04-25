import matplotlib.pyplot as plt
import random


x = arr = [random.randint(-100, 100) for i in range(1000)]
y = arr = [random.randint(-100, 100) for i in range(1000)]
color = arr = [random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']) for i in range(1000)]

plt.scatter(x, y, c=color)

plt.axis([-100,100,-100,100])
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

plt.show()