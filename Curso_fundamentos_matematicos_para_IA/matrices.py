import numpy as np

m1= np.matrix([[1,0,3],
              [-4,3,7],
              [2,-2,-5]])

m2= np.matrix([[2,1,0],
              [3,1,-2],
              [0,-1,-2]])

m3= m1*m2

print(m3)