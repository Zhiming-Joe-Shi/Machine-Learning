#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import numpy as np
#CLASSIC MULTIVARIATE LINEAR REGRESSION FORM: y = f(X) = W*X + b
#CAPITAL LETTER denotes vector, lowercase letter denotes scalar
Xy = np.genfromtxt("sheet.csv", delimiter=",", dtype=float)
m = len(Xy)    #rows
n = len(Xy[0]) #columns
X = Xy[...,:-1] #size of m × n-1 
y = Xy[....-1]  #size of m × 1
X1 = np.append(X, np.ones((m,1)), axis=1)
wb = np.zeros(1,n)
STEP_SIZE = float(input("Set your learning rate. STEP_SIZE = "))
#ALGORITHM
isMin = False
prevDistSum = None
while isMin == False:
    dW = [0]*(n-1) #(re-)initialize local variables
    db = 0
    wx = [0]*(m)
    distSum = 0
    for j in range(n-1):
        for i in range(m):
            wx[i] += W[j]*X[i][j]
            dW[j] += (1/m)*X[i][j]*(wx[i] + b - y[i])
    for i in range(m):
        db += (1/m)*(wx[i] + b - y[i])
        distSum += (1/(2*m))*(wx[i] + b - y[i])**2
    if prevDistSum == None or distSum / prevDistSum <= 0.9999999999:
        prevDistSum = distSum
        for j in range(n-1):
            W[j] -= STEP_SIZE * dW[j]
        b -= STEP_SIZE * db
    elif distSum / prevDistSum > 0.9999999999:
        isMin = True
#print out the outputs
print("---OUTPUT---")
for i, val in enumerate(W):
    print("w_%d = %.4f" % (i+1, val))
print("b = %.4f" % b)
print("The minimized squared sum = %.4f" % distSum)

#可决定系数(Coefficient of determination)计算
ySum = 0
for i in range(m):
    ySum += y[i]
y_avg = ySum / m

y_fit = pass
#Author: Zhiming Shi
