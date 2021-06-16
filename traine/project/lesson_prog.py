import matplotlib.pyplot as plt
import numpy as np


def E2(q1, q2, r, x, y):
    try:
        l = 1
        k = 9 * 10 ** 9
        v2 = (k * q1) / ((x + r / 2) ** 2 + y ** 2)
        v3 = (k * q2) / ((x - r / 2) ** 2 + y ** 2)
        x2 = (x + r / 2) * (v2 / ((r / 2 + x) ** 2 + y ** 2) ** 0.5)
        y2 = y * (v2 / ((r / 2 + x) ** 2 + y ** 2) ** 0.5)

        x3 = (x - r / 2) * (v3 / ((x - r / 2) ** 2 + y ** 2) ** 0.5)
        y3 = y * (v3 / ((r / 2 - x) ** 2 + y ** 2) ** 0.5)
    except RuntimeWarning:
        pass
    finally:
        return (x2 + x3) * l, (y2 + y3) * l


size = 4
qual = 0.5
gr = np.mgrid[-size:(size + 1):qual, -size:(size + 1):qual]
xg, yg = np.array(gr[0]).reshape(-1), np.array(gr[1]).reshape(-1)

q1 = 1 * 10 ** (-10)
q2 = -1 * 10 ** (-10)
r = 5
size = 5
plt.figure(dpi=250)
plt.xlim(-(size + 1), (size + 1))
plt.ylim(-(size + 1), (size + 1))
plt.gca().set_aspect('equal', adjustable='box')
plt.scatter([-r / 2, r / 2], [0, 0])
E = 0
n = 30

for x, y in zip(xg, yg):
    x1, y1 = E2(q1, q2, r, x, y)

    plt.scatter([x, x1 + x], [y, y1 + y], s=0, c='w')

    plt.arrow(x, y, x1 * 10, y1 * 10, color='blue', head_width=0.1, linewidth=0.2)
plt.show()