import numpy

a = numpy.array([1,2,3,4])

print(a)

import time
a = numpy.random.rand(1000000)
b = numpy.random.rand(1000000)

tic = time.time()
c = numpy.dot(a,b) #It is inner product of vectors
toc = time.time()

print (c)
print("Vectorized version: " + str(1000*(toc-tic)) + "ms.")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print (c)
print("For loop: " + str(1000*(toc-tic)) + "ms.")
