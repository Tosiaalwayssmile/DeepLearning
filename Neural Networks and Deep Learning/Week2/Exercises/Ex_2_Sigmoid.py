import math

""" This function applies the exponential function to a real number """
def basic_sigmoid(x):
    s = 1 / (1 + math.exp(-x))
    return s

print(basic_sigmoid(3))

import numpy 

""" Using numpy allows us to apply the exponential function to every element of x. Even if x is a row vector or a matrix. """
x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def np_sigmoid(x):
    s = 1 / (1 + numpy.exp(-x))
    return s

print(np_sigmoid(x))
