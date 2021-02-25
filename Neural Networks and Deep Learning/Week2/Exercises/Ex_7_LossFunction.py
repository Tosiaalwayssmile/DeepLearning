import numpy as np

""" L1 loss """
def L1(yhat, y):
    loss = np.sum(abs(y - yhat))
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))

""" Loss function 2"""
def L2(yhat, y):
    loss = np.sum(np.dot(y-yhat, y-yhat)) 
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))