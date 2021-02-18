# Cost function #
#J = 0

import numpy 

w.T = 0, x = 0, b = 0

# Z = w^T * X + b
Z = numpy.dot(w.T, X) + b #broadcasting

A = sig(Z)

dZ = A - Y

dw = 0
dw = 1/m * X * dZ.T

db = 0
db = 1/m * numpy.sum(dZ)

#dw = numpy.zeros(n-x,1)

#gradient descent

w: w - alpha * dw
b: b - alpha * db

