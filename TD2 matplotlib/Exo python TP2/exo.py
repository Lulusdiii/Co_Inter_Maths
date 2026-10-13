from pylab import *
listex = []
listey = []
for x in range(5, 15):
    listex.append(x)
    listey.append(3)
plot(listex, listey, '.k')
xlim(0, 20)
ylim(2.0, 4.0)
show()