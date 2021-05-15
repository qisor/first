import numpy as np
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False
pyplot.rcParams["font.style"] = "italic"

pyplot.figure(dpi=320)
x = np.array(np.arange(-10, 10, 0.5))
y = np.sin(x)
y1 = np.cos(x)
s = np.tan(x)
y2 = x * 2

pyplot.rc("font", family="SimHei")
pyplot.title("picture")
pyplot.plot(x, y, "*r-", label="sine")
pyplot.plot(x, y1, "*g-", label="cosine")
pyplot.plot(x, s, color="blue", linewidth=1.5, linestyle="-", label="tan")
pyplot.bar(x, y2, color='c', align='center', label="柱图")
pyplot.hist(x, bins=[-7, -4, -1, 3, 6, 10], color='m', label="直方图", )
pyplot.legend(loc='lower left')
pyplot.show()
