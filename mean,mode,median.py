import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,88]

x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
p = numpy.std(speed)
q = numpy.var(speed)
r = numpy.percentile(speed, 75)
s = numpy.percentile(speed, 90)
print("Mean : ",x)
print("Median : ",y)
print("Mode : ",z)
print("Starderd de. : ",p)
print("Vrience : ",q)
print("Percentile : ",r)
print("Percentile : ",s)