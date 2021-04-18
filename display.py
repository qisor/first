import numpy as np
from matplotlib import pyplot

pyplot.figure(dpi=320)
x = np.array(np.arange(-10, 10, 0.5))
y = np.sin(x)
y1 = np.cos(x)
s = np.tan(x)
y2 = x * 2
pyplot.title("picture")
pyplot.plot(x, y, "*r-", label="sine")
pyplot.plot(x, y1, "*g-", label="cosine")
pyplot.plot(x, s, color="blue", linewidth=1.5, linestyle="-", label="tan")
pyplot.bar(x, y2, color='c', align='center', label="柱图")
pyplot.hist(x, bins=[0, 2, 4, 6, 8, 10], color='y', label="直方图")
pyplot.legend(loc='lower left')
pyplot.show()
