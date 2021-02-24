import numpy

a = numpy.array([1,2,3,4])

print(a)

import time
a = numpy.random.rand(1000000)
b = numpy.random.rand(1000000)

tic = time.time()
c = numpy.dot(a,b) #It is inner product of vectors
toc = time.time()
VecVer = 1000*(toc-tic)
print (c)
print("Vectorized version: " + str(VecVer) + "ms.")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print (c)
FL = 1000*(toc-tic)
print("For loop: " + str(FL) + "ms.")

print("Vectorized version is " + str(FL/VecVer) + " times faster.")

a = numpy.random.randn(3, 3)
b = numpy.random.randn(3, 1)
c = a*b
print(c)



