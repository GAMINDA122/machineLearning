import numpy
import matplotlib.pyplot as plt


y = numpy.random.normal(5.0, 1.0, 100000)


plt.hist(y, 100)
plt.show()