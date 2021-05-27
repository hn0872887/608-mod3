
import statistics
import math

a = statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
b = statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
c = math.sqrt(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))

print("pvariance: ", a)
print("pstdev: ", b)
print("sqrt: ", c)