import numpy as np
 
""" Function that normalizes each row of the matrix x (to have unit length). """
def normalizeRows(x):
   
    # Compute x_norm as the norm 2 of x. 
    x_norm = np.linalg.norm(x, ord = 2, axis = 1, keepdims = True)
    
    # Divide x by its norm.
    x = x / x_norm

    # x -- The normalized (by row) numpy matrix. 
    return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])

print("normalizeRows(x) = " + str(normalizeRows(x)))