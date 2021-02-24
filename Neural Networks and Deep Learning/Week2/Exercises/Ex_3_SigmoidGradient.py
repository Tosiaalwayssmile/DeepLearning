import numpy

def np_sigmoid(x):
    s = 1 / (1 + numpy.exp(-x))
    return s

""" Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x. """
def sigmoid_derivative(x):
    
    s = np_sigmoid(x)

    """ ds -- Computed gradient. """
    ds = s*(1-s) 
    
    return ds

x = numpy.array([1, 2, 3])

print ("sigmoid_derivative(x) = " + str(sigmoid_derivative(x)))