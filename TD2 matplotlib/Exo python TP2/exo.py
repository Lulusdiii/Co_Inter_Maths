from pylab import *
listex = []
listey = []
for y in range(10, 20):
for x in range(5, 15):
listex.append(x)
listey.append(y)
plot(listex, listey, '.k')
xlim(0, 20)
ylim(0, 30)
show()